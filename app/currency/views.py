from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View, TemplateView
from django.core.mail import send_mail
from currency import choices, consts
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from currency.utils import generate_password as gp
from currency.tasks import send_email_in_background

from django.http import HttpResponse, JsonResponse

from currency.forms import RateForm, ContactUsCreate
from currency.models import Rate, ContactUs, Bank
from django_filters.views import FilterView
from currency.filters import RateFilter


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def index(request):
    return render(request, 'index.html')


class RateListView(FilterView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all().select_related('bank')
    paginate_by = 25
    filterset_class = RateFilter


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


def get_latest_rates():
    if consts.CACHE_KEY_LATEST_RATES in cache:
        return cache.get(consts.CACHE_KEY_LATEST_RATES)

    object_list = []
    for bank in Bank.objects.all():
        for ct_value, ct_display in choices.RATE_TYPE_CHOICES:
            latest_rate = Rate.objects \
                .filter(type=ct_value, bank=bank).order_by('-created').first()
            if latest_rate is not None:
                object_list.append(latest_rate)

    cache.set(consts.CACHE_KEY_LATEST_RATES, object_list, 60 * 60 * 8)
    return object_list


# @method_decorator(cache_page(60 * 60 * 8), name='dispatch')
class LatestRates(TemplateView):
    template_name = 'latest_rates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_latest_rates()
        return context


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


# class RateListApi(View):
#     def get(self, request):
#         rates = Rate.objects.all()
#         results = []
#         for rate in rates:
#             results.append({
#                 'id': rate.id,
#                 'sale': float(rate.sale),
#                 'buy': float(rate.buy),
#                 'bank': rate.bank_id,
#             })
#         import json
#         return JsonResponse(results, safe=False)
#         # return HttpResponse(json.dumps(results), content_type='application/json')
