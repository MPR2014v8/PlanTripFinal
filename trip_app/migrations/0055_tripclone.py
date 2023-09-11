# Generated by Django 4.2.1 on 2023-09-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0054_trip_date_end_trip_date_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripClone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, blank=True, null=True)),
                ('tripClone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tripClone', to='trip_app.trip')),
            ],
        ),
    ]
