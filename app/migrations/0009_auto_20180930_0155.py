# Generated by Django 2.0.7 on 2018-09-29 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180930_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='Last_Update',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 30, 1, 55, 53, 300675)),
        ),
        migrations.AlterField(
            model_name='clients',
            name='Time_Left',
            field=models.DurationField(),
        ),
    ]
