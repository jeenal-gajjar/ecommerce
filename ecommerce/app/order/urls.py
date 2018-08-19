from django.conf.urls import url
from .views import OrderView


urlpatterns = [
   url(r'^order/$', OrderView.as_view(), name='order'),
]
