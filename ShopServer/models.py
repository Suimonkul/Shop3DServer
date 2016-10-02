# coding=utf-8
from django.db import models

# Create your models here.
from django.db.models import Model


class Advert(models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=120, null=True, blank=False, unique=False)
    image = models.CharField(null=True, max_length=10000)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title


class CategoryProduct(models.Model):
    name = models.CharField(max_length=120, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=50, null=True)
    cover = models.CharField(max_length=10000, null=True, help_text="Size 640x640")
    image_first = models.CharField(max_length=10000, null=True, help_text="Size 960x640")
    image_second = models.CharField(max_length=10000, null=True, help_text="Size 960x640")
    image_third = models.CharField(max_length=10000, null=True, help_text="Size 960x640")
    order = models.IntegerField(null=True)
    description = models.CharField(max_length=320, null=True)
    category = models.ForeignKey(CategoryProduct)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title
