# Generated by Django 4.2.1 on 2023-07-17 03:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2023, 7, 17, 10, 36, 50, 875155))),
                ('payment_status', models.BooleanField(default=False)),
                ('change_datetime', models.DateTimeField(default=datetime.datetime(2023, 7, 17, 10, 36, 50, 875155))),
                ('upload_img', models.ImageField(upload_to='')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
