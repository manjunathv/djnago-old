from django.conf.urls import patterns, url

from diaglitica import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^analytics',views.analytics,name='analytics')
)