# Generated by Django 4.2.1 on 2023-07-17 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0016_alter_payment_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 13, 6, 32, 172699)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 13, 6, 32, 172699)),
        ),
    ]
