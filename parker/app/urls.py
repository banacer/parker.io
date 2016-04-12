from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('index',views.index),
    url('layout', views.layout),
    url('signup',views.signup,name='signup'),
    url('signin', views.signin),
    url('signout', views.signout),
    url(r'^users/(?P<user_id>[0-9]+)/$',views.getuser,name='User'),
    url(r'^$', views.index, name='index'),
    url('api/dataservice/checkUnique',views.username_exist,name='checkunique'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)