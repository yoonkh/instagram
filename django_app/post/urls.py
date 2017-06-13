from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail),


]