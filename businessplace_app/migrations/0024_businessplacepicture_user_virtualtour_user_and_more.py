# Generated by Django 4.2.1 on 2023-07-17 05:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('businessplace_app', '0023_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessplacepicture',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pic_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualtour',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vr_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 12, 15, 50, 927268)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 12, 15, 50, 928272)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 12, 15, 50, 928272)),
        ),
    ]
