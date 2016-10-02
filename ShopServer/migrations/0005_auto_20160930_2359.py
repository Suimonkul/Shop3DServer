# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopServer', '0004_auto_20160917_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.CharField(help_text=b'Size 640x640', max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_first',
            field=models.CharField(help_text=b'Size 960x640', max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_second',
            field=models.CharField(help_text=b'Size 960x640', max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_third',
            field=models.CharField(help_text=b'Size 960x640', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=320, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
