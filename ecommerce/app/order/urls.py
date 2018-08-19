from django.conf.urls import url
from .views import OrderView, OrderUpdateView


urlpatterns = [
   url(r'^order/$', OrderView.as_view(), name='order'),
   url(r'^order/(?P<pk>[0-9]+)/$', OrderUpdateView.as_view(), name='order_update'),
]
