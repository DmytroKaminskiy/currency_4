from django import forms

from currency.models import Rate, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            # 'type',
            'sale',
            'buy',
            'bank',
        )


class ContactUsCreate(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )

    # def save(self, commit=True):
    #     print('Form Save\n' * 10)
    #     return super().save(commit)
