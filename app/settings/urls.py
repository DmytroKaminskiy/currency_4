from django.contrib import admin
from django.urls import path

from currency.views import generate_password


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('gen-pass/', generate_password()),
    path('gen-pass/', generate_password),
]
