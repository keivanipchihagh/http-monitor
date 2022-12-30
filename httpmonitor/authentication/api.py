from django.contrib.auth import login
from .serializers import UserSerializer
from knox.auth import TokenAuthentication
from knox.views import LoginView, LogoutView
from rest_framework import permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .models import User


class SignInView(LoginView):
    """ Signs in user (login) """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication]

    def post(self, request, format = None):
        serializer = AuthTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(SignInView, self).post(request, format = None)


class SignUpApi(generics.CreateAPIView):
    """Signs up user (register)  """
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]


class SignOutApi(LogoutView):
    """ Signs out user """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication]


class SignOutAllApi(LogoutView):
    """ Signs out user from everywhere """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication]