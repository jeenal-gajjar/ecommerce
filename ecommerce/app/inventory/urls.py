from django.conf.urls import url
from .views import ProductView, ProductUpdateView


urlpatterns = [
   url(r'^product/$', ProductView.as_view(), name='product_list'),
   url(r'^product/(?P<pk>[0-9]+)/$', ProductUpdateView.as_view(), name='product_update'),
]
