from django.conf.urls import url
from hello_world import views

urlpatterns = [ url(r'^$', views.index, name='index'), url(r'better/$',views.better, name='better'),


 ]


