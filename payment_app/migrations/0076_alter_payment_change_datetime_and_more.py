# Generated by Django 4.2.1 on 2023-09-01 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0075_alter_payment_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 22, 7, 14, 460326)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 22, 7, 14, 460326)),
        ),
    ]
