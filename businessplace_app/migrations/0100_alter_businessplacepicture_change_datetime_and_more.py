# Generated by Django 4.2.1 on 2023-09-04 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0099_alter_businessplacepicture_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 22, 14, 17, 893522)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 22, 14, 17, 894519)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 22, 14, 17, 894519)),
        ),
    ]