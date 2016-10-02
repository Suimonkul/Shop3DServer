from django.contrib import admin

from ShopServer.models import Advert, Product, CategoryProduct


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'active']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
