from django.core.management.base import BaseCommand
from currency.models import Rate, Bank

import random
from django.db import transaction


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        b = Bank.objects.last()

        # print('Before Count', Rate.objects.count())
        # try:
        #     with transaction.atomic():
        #         rate1 = Rate.objects.create(buy=21, sale=21, bank=b, type=0)
        #         rate2 = Rate.objects.create(buy=21, sale=21, bank=b, type=0)
        # finally:
        #     print('After Count', Rate.objects.count())

        # with transaction.atomic():
        #     sid = transaction.savepoint()
        #     print('Before Count', Rate.objects.count())

            # rate1 = Rate.objects.create(buy=21, sale=21, bank=b, type=0)

            # transaction.savepoint_commit(sid)
            # transaction.savepoint_rollback(sid)
            # print('After Count', Rate.objects.count())
