from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

urlpatterns = [
    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
    # Upload Picture App view urls
    url(r'^uploadPic/',include('myproject.uploadPic.urls')),
    # start from list.html urls
    url(r'^$', RedirectView.as_view(url='/uploadPic/list/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Save image to media/documents/Y/m/d/
