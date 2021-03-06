# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 14:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=33)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField()),
                ('visit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('visit_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.Visit'),
        ),
    ]
