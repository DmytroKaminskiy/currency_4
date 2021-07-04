from celery import shared_task
from django.core.mail import send_mail
from currency import choices
from currency import consts

import requests

from currency.utils import to_decimal


def _get_privatbank_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task
def parse_privatbank():
    from currency.models import Rate, Bank

    bank = Bank.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)
    currencies = _get_privatbank_currencies(bank.url)

    # available_currencies = frozenset(('USD', 'EUR'))
    # available_currency_types = ('USD', 'EUR')
    available_currency_types = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    for curr in currencies:
        currency_type = curr['ccy']
        if currency_type in available_currency_types:
            currency_type = available_currency_types[curr['ccy']]

            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(
                bank=bank, type=currency_type
            ).order_by('created').last()
            # check if new rate should be create

            if (
                    previous_rate is None or  # rate does not exists, create the first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                print(f'New rate was created: {sale} {buy}')
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
            else:
                print(f'Rate already exists:  {sale} {buy}')


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 60,
    },
)
def send_email_in_background(body):
    send_mail(
        'Contact Us from Client',
        body,
        'testtestapp454545@gmail.com',
        ['fenderoksp@gmail.com'],
        fail_silently=False,
    )
