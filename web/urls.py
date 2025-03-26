from django.urls import path
from .views import index, price_list

urlpatterns = [
    path('', index, name='home'),
    path('price/', price_list, name='price'),
]
