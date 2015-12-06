from django.conf.urls import patterns, url

# define a action url for list post method
urlpatterns = patterns('myproject.uploadPic.views',
    url(r'^list/$', 'list', name='list')
)
