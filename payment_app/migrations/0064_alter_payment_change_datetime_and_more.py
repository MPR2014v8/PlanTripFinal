# Generated by Django 4.2.1 on 2023-08-30 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0063_alter_payment_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 0, 10, 20, 814201)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 0, 10, 20, 814201)),
        ),
    ]
