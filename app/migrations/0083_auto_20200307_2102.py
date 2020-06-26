# Generated by Django 3.0.3 on 2020-03-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0082_auto_20200307_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='rates',
            options={'verbose_name': 'Rate', 'verbose_name_plural': 'Rates'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterModelOptions(
            name='vouchers',
            options={'verbose_name': 'Voucher', 'verbose_name_plural': 'Vouchers'},
        ),
        migrations.AlterModelOptions(
            name='whitelist',
            options={'verbose_name': 'Whitelisted Device', 'verbose_name_plural': 'Whitelisted Devices'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='MAC_Address',
            field=models.CharField(max_length=255, unique=True, verbose_name='MAC Address'),
        ),
        migrations.AlterField(
            model_name='coinqueue',
            name='Client',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='Denom',
            field=models.IntegerField(help_text='Coin denomination corresponding to specified coinslot pulse.', verbose_name='Denomination'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='Minutes',
            field=models.DurationField(help_text='Internet access duration in hh:mm:ss format', verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='Pulse',
            field=models.IntegerField(help_text="Coinslot pulse count. Don't change this if you dont know what you're doing"),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_client',
            field=models.CharField(blank=True, help_text='Voucher code user. * Optional', max_length=50, null=True, verbose_name='Client'),
        ),
    ]