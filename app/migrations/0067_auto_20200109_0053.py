# Generated by Django 2.2.7 on 2020-01-08 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_auto_20200108_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='Last_Updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
