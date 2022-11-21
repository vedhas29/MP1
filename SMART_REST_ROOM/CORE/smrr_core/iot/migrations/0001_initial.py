# Generated by Django 4.0.6 on 2022-11-13 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flutter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='iot_devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_id', models.CharField(max_length=50, verbose_name='mac_id')),
                ('device_name', models.CharField(max_length=50, verbose_name='device_name')),
                ('senses_gas', models.CharField(max_length=50, verbose_name='senses_gas')),
            ],
        ),
        migrations.CreateModel(
            name='iot_log',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False, verbose_name='log_id')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='time')),
                ('gas01', models.DecimalField(decimal_places=8, max_digits=12, verbose_name='gas01')),
                ('gas02', models.DecimalField(decimal_places=8, max_digits=12, verbose_name='gas02')),
                ('gas03', models.DecimalField(decimal_places=8, max_digits=12, verbose_name='gas03')),
                ('gas04', models.DecimalField(decimal_places=8, max_digits=12, verbose_name='gas04')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flutter.rooms', verbose_name='rooms')),
            ],
        ),
    ]
