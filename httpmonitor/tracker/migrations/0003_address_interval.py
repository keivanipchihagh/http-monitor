# Generated by Django 4.1.4 on 2022-12-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_address_alter_request_track_delete_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='interval',
            field=models.BigIntegerField(default=5, verbose_name='Interval for requests in minutes'),
        ),
    ]
