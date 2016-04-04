from django.conf.urls import url

from . import views

urlpatterns = [
    url('hola',views.hola,name='hola'),
    url('signup',views.signup,name='signup'),
    url(r'^users/(?P<user_id>[0-9]+)/$',views.getuser,name='User'),
    url(r'^$', views.index, name='index'),
]