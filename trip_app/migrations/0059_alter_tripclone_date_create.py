# Generated by Django 4.2.1 on 2023-09-11 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0058_remove_tripclone_date_tripclone_date_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripclone',
            name='date_create',
            field=models.DateField(auto_created=True, blank=True, default=datetime.datetime(2023, 9, 11, 21, 12, 16, 169974), null=True),
        ),
    ]
