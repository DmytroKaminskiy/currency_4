from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from currency.utils import generate_password as gp

from django.http import HttpResponse

from currency.forms import RateForm
from currency.models import Rate, ContactUs


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def index(request):
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
    success_url = reverse_lazy('index')
    # template_name = 'contact-us-create.html'
