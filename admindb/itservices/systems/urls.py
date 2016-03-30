from django.conf.urls import patterns
from django.conf.urls import url
from itservices.systems import views

urlpatterns = patterns('',
    url(r'^importsystems_list$', views.importsystems_list, name='importsystems_list'),
    # url(r'^importsystems_list$', views.importsystems_list, name='importsystems_list'),
               
    # url(r'^system_detail/(?P<system_id>\d+)/$', views.system_detail, name='system_detail'),
    )
