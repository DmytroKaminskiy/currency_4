from django.core.management.base import BaseCommand
from currency.models import Rate

import random


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        for index in range(100):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=index,
                buy=index + 1,  # generate random decimal between 20.00 up to 29.99
                source='monobank',  # select random from ['monobank', 'privatbank', 'vkurse']
            )
            # rate = Rate(
            #     type='usd',
            #     sale=index,
            #     buy=index + 1,
            #     source='monobank',
            # )
            # rate.save()

            # ContactUs (Faker)
