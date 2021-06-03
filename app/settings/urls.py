from currency.views import generate_password, rate_list, rate_details

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('gen-pass/', generate_password()),
    path('gen-pass/', generate_password),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
]
