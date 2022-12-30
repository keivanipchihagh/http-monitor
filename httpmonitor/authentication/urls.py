from django.urls import path
from .api import *
from knox import views as knox_views


urlpatterns = [
    path(route = 'signup/', view = SignUpApi.as_view(), name = 'signup'),
    path(route = 'signin/', view = SignInView.as_view(), name = 'signin'),    
    path(route = 'signout/', view = SignOutApi.as_view(), name = 'signout'),
]