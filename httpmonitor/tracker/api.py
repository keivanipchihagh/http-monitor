from django.core import serializers
from rest_framework import status
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Address, Request
from .forms import AddressForm

class AddAddress(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format = None):
        form = AddressForm(request.data)
        if form.is_valid():
            data = form.cleaned_data
            Address.objects.create(
                url = data["url"],
                threshold = data["threshold"],
                interval = data["interval"],
                user_id = self.request.user.id
            )
            response, code = None, status.HTTP_201_CREATED
        else:
            response, code = form.errors, status.HTTP_200_OK

        return Response(data = response, status = code)


class GetAddresses(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format = None):
        addresses = Address.objects.filter(user_id = self.request.user.id).values("url", "interval", "threshold")
        return Response(data = addresses, status = status.HTTP_200_OK)


class GetAddressStatus(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format = None):
        requests = Request.objects.raw(f"""
            select
                1 as id,
                url,
                status_code,
                count (*) as count
            from
                tracker_request
            inner join tracker_address
                on tracker_address.id = tracker_request.track_id
            inner join authentication_user
                on authentication_user.id = tracker_address.user_id
            where
                authentication_user.id = {self.request.user.id}
                and tracker_request.created_at > current_date - interval '24 hours'
            group by
                url, status_code
        """)

        data = {}
        for request in requests:
            if request.url in data.keys():
                data[request.url][request.status_code] = request.count
            else:
                data[request.url] = {request.status_code: request.count}

        return Response(data = data, status = status.HTTP_200_OK)
