from .api import *
from django.urls import path


urlpatterns = [
    path(route = 'add-address/', view = AddAddress.as_view(), name = 'add-address'),
    path(route = 'get-addresses/', view = GetAddresses.as_view(), name = 'get-addresses'),
    path(route = 'get-address-status/', view = GetAddressStatus.as_view(), name = 'get-address-status'),
]