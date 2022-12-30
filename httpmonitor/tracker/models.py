from django.db import models


class Address(models.Model):
    """ Addresses that are to be tracked """

    url = models.CharField(
        max_length = 300,
        null = False,
        verbose_name = "URL"
    )

    threshold = models.BigIntegerField(
        null = False,
        verbose_name = "Number of errors to tolerate"
    )

    interval = models.BigIntegerField(
        null = False,
        default = 5,
        verbose_name = "Interval for requests in minutes"
    )

    created_at = models.DateTimeField(
        null = False,
        auto_now_add = True,
        verbose_name = "Created at"
    )

    user = models.ForeignKey('authentication.User', on_delete = models.CASCADE)


class Request(models.Model):
    """ Requests made to Addresses """

    status_code = models.BigIntegerField(
        null = False,
        verbose_name = "Result status code"
    )

    created_at = models.DateTimeField(
        null = False,
        auto_now_add = True,
        verbose_name = "Created at"
    )

    track = models.ForeignKey(Address, on_delete = models.CASCADE)