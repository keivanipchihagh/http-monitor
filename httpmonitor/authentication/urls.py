from .api import *
from django.urls import path


urlpatterns = [
    path(route = 'signup/', view = SignUpApi.as_view(), name = 'signup'),
    path(route = 'signin/', view = SignInView.as_view(), name = 'signin'),    
    path(route = 'signout/', view = SignOutApi.as_view(), name = 'signout'),
    path(route = 'signout-all/', view = SignOutAllApi.as_view(), name = 'signout'),
]