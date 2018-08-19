from django.conf.urls import url
from .auth import SignUp, Login, Logout


urlpatterns = [
   url(r'^signup/$', SignUp.as_view(), name='signup'),
   url(r'^login/$', Login.as_view(), name='login'),
   url(r'^logout/$', Logout.as_view(), name='logout'),
]
