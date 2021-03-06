from django.db import models
from currency import choices


class Bank(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(
        max_length=64,
        unique=True,
    )
    url = models.URLField()
    original_url = models.URLField()

    def __str__(self):
        return f'Bank {self.name}'


class Rate(models.Model):
    # def get_{field_name}_display()
    type = models.PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    bank = models.ForeignKey(
        Bank,
        related_name='rates',
        on_delete=models.CASCADE,
    )
    # bank = models.ForeignKey('currency.Bank')

    def __str__(self):
        return f'Rate id: {self.id} {self.bank_id}'


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     print('ContactUs Model save')
    #     return super().save(*args, **kwargs)

class Analytics(models.Model):
    path = models.CharField(max_length=255)
    counter = models.PositiveBigIntegerField()
    request_method = models.PositiveSmallIntegerField(
        choices=choices.REQUEST_METHOD_CHOICES)

    class Meta:
        unique_together = [
            ['path', 'request_method'],
        ]

"""
OtO - OneToOne
OTM - OneToMany
MtM - many To Many
"""