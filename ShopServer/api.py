from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource

from ShopServer.models import Advert, Product, CategoryProduct


class ADVResource(ModelResource):
    class Meta:
        limit = 0

        queryset = Advert.objects.all()
        resource_name = 'advert'


class CategoryResource(ModelResource):
    class Meta:
        limit = 0

        queryset = CategoryProduct.objects.all()
        resource_name = 'category'


class ProductResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', null=True)

    class Meta:
        limit = 8

        queryset = Product.objects.all()
        resource_name = 'product'
        filtering = {
            'title': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
        }

        class_paginator = Paginator
