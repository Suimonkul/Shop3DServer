# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopServer', '0002_advert_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=120, null=True)),
                ('image', models.CharField(max_length=10000, null=True)),
                ('order', models.IntegerField(max_length=120, null=True)),
                ('description', models.CharField(max_length=10000, null=True)),
                ('category', models.ForeignKey(to='ShopServer.CategoryProduct')),
            ],
        ),
    ]
