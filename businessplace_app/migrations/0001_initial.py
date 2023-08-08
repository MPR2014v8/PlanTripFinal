# Generated by Django 4.2.1 on 2023-07-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('detaill', models.TextField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.URLField(max_length=100)),
                ('address', models.TextField()),
                ('timeOpen', models.TimeField()),
                ('timeClose', models.TimeField()),
                ('website', models.URLField()),
                ('created_datetime', models.DateTimeField()),
                ('change_datetime', models.DateTimeField()),
            ],
        ),
    ]
