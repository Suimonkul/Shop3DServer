# coding=utf-8
from django.db import models

# Create your models here.
from django.db.models import Model


def image_upload_to(instance, filename):
    return "images/%s" % filename


class Advert(models.Model):
    active = models.BooleanField(verbose_name="Отобразить", default=False)
    title = models.CharField(verbose_name="Назание", max_length=120, null=True, blank=False, unique=False)
    image = models.ImageField(null=True, help_text="Size 960x640")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title


class CategoryProduct(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=120, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(verbose_name="Отобразить", default=False)
    title = models.CharField(verbose_name="Назание", max_length=50, null=True)
    cover = models.ImageField(verbose_name="Обложка", null=True, help_text="Size 640x640")
    image_first = models.ImageField(verbose_name="Изобр. 1", null=True, help_text="Size 960x640")
    image_second = models.ImageField(verbose_name="Изобр. 2", null=True, help_text="Size 960x640")
    image_third = models.ImageField(verbose_name="Изобр. 3", null=True, help_text="Size 960x640")
    order = models.IntegerField(verbose_name="Цена", null=True)
    description = models.CharField(verbose_name="Описание", max_length=320, null=True)
    category = models.ForeignKey(CategoryProduct, verbose_name="Категория")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title
