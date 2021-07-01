from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.mail import send_mail

from currency.utils import generate_password as gp
from currency.tasks import send_email_in_background

from django.http import HttpResponse

from currency.forms import RateForm, ContactUsCreate
from currency.models import Rate, ContactUs


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def index(request):
    print('INDEX')
    return render(request, 'index.html')


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


def rate_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('currency:rate-list'))
            return redirect('currency:rate-list')

    elif request.method == 'GET':
        form = RateForm()

    context = {
        'message': 'Rate Create',
        'form': form,
        'count': Rate.objects.count(),
    }
    return render(request, 'rate_create.html', context=context)


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')


class CreateContactUs(CreateView):
    model = ContactUs
    fields = (
        'email_from',
        'subject',
        'message',
    )
    # form_class = ContactUsCreate
    success_url = reverse_lazy('index')

    # template_name = 'contact-us-create.html'

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}

        Message:
        {data['message']}
        '''

        send_email_in_background.delay(body)

        # from .tasks import print_hello_world
        # print_hello_world.delay()

        return super().form_valid(form)
