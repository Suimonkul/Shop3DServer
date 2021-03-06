from django.conf.urls import include, url, patterns
from django.contrib import admin
from tastypie.api import Api

from ServerShop3d import settings
from ShopServer.api import ADVResource, CategoryResource, ProductResource

v1 = Api(api_name='v1')
v1.register(ADVResource())
v1.register(ProductResource())
v1.register(CategoryResource())

urlpatterns = patterns('',
                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^admin/', admin.site.urls),
                       url(r'^api/', include(v1.urls)),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       )
