# Generated by Django 4.2.1 on 2023-09-02 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0050_alter_trip_change_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='change_datetime',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='created_datetime',
        ),
        migrations.RemoveField(
            model_name='tripdetail',
            name='change_datetime',
        ),
        migrations.RemoveField(
            model_name='tripdetail',
            name='created_datetime',
        ),
    ]
