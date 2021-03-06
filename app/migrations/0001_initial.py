# Generated by Django 2.0.7 on 2018-09-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP_Address', models.CharField(max_length=15, verbose_name='IP')),
                ('MAC_Address', models.CharField(max_length=255, verbose_name='MAC')),
                ('Device_Name', models.CharField(max_length=255, verbose_name='Device')),
                ('Status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SlotStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField()),
            ],
        ),
    ]
