# Generated by Django 4.2.1 on 2023-07-19 17:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('businessplace_app', '0032_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 0, 32, 48, 923288)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 0, 32, 48, 924304)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 0, 32, 48, 924304)),
        ),
        migrations.CreateModel(
            name='RatingAndComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=5)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('change_datetime', models.DateTimeField(default=datetime.datetime(2023, 7, 20, 0, 32, 48, 925319))),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='businessplace_app.businessplace')),
                ('rac_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rac_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
