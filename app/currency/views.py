from currency.utils import generate_password as gp

from django.http import HttpResponse


def generate_password(request):
    password = gp()
    return HttpResponse(password)
