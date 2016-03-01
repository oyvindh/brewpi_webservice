# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controller', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('uri', models.CharField(help_text='A device URI such as onewire://182377282', max_length=255)),
                ('slot', models.PositiveIntegerField(blank=True, help_text='The slot ID assigned paired with the Controller', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('uri', models.CharField(help_text='A device URI such as onewire://182377282', max_length=255)),
                ('slot', models.PositiveIntegerField(blank=True, help_text='The slot ID assigned paired with the Controller', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DS2413Actuator',
            fields=[
                ('actuator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='device.Actuator')),
                ('pio', models.PositiveIntegerField(choices=[(0, 'A'), (1, 'B')], help_text='PIO number of the addressable switch')),
                ('inverted', models.BooleanField(default=False, help_text='If the switch is inverted')),
            ],
            options={
                'verbose_name': 'DS2413',
                'verbose_name_plural': 'DS2413',
            },
            bases=('device.actuator',),
        ),
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='device.Sensor')),
                ('value', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('device.sensor',),
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='device.Sensor')),
                ('value', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('device.sensor',),
        ),
        migrations.AddField(
            model_name='sensor',
            name='controller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='controller.Controller'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_device.sensor_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='controller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actuators', to='controller.Controller'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_device.actuator_set+', to='contenttypes.ContentType'),
        ),
    ]
