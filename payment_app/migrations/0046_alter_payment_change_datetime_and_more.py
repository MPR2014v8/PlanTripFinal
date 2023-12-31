# Generated by Django 4.2.1 on 2023-08-11 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0045_payment_upload_img_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 8, 40, 22, 776143)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 8, 40, 22, 776143)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='upload_img_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
