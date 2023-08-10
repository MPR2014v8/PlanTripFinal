# Generated by Django 4.2.1 on 2023-08-10 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0053_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 0, 43, 17, 194145)),
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 0, 43, 17, 195144)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='businesstype',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 0, 43, 17, 196209)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 0, 43, 17, 195144)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]