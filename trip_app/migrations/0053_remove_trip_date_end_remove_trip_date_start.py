# Generated by Django 4.2.1 on 2023-09-02 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0052_trip_date_end_trip_date_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='date_start',
        ),
    ]
