from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/$', views.detail),
    url(r'^about/$', views.about),
    url(r'^post/$', views.post),
    url(r'^contact/$', views.contact),
    url(r'^send/$', views.send),
]
