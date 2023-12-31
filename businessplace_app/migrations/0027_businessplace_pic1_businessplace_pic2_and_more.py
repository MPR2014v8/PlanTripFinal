# Generated by Django 4.2.1 on 2023-07-17 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0026_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessplace',
            name='pic1',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessplace',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='businessplace',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='businessplace',
            name='vr',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 13, 5, 19, 515051)),
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='detaill',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='timeClose',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='timeOpen',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 13, 5, 19, 516086)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='detaill',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businesstype',
            name='detaill',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 13, 5, 19, 516086)),
        ),
    ]
