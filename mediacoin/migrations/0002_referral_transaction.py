# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 23:28
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mediacoin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_id', models.CharField(max_length=36)),
                ('web3addr', models.CharField(max_length=50)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.DecimalField(decimal_places=8, default=Decimal('0.0'), max_digits=16)),
                ('address', models.CharField(max_length=50)),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediacoin.Referral')),
            ],
        ),
    ]
