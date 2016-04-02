from django.conf.urls import url

from . import views

urlpatterns = [
    url('hola',views.hola,name='hola'),
    url(r'^$', views.index, name='index'),
]