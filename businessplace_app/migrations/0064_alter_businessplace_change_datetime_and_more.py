# Generated by Django 4.2.1 on 2023-08-23 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0063_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 24, 1, 39, 43, 441973), null=True),
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 1, 39, 43, 442971)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 1, 39, 43, 444964)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 1, 39, 43, 443966)),
        ),
    ]
