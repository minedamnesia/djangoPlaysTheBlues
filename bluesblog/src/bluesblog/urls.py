from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from accounts.views import UserRegistrationView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user-registration'),
]
