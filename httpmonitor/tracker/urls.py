from .api import *
from django.urls import path


urlpatterns = [
    path(route = 'example/', view = ExampleView.as_view(), name = 'signup'),
]