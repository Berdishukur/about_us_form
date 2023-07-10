from django.urls import path
from .views import *
urlpatterns = [
    path('', customer_form, name='customers-form'),
    path('list/', customer_form, name='customers-list'),
]