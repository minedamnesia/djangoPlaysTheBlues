from django.conf.urls import include, url
from django.contrib import admin

from organizer import urls as organizer_urls
from .views import redirect_root

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(organizer_urls)),
]