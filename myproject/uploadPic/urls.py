from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.uploadPic.views',
    url(r'^list/$', 'list', name='list')
)
