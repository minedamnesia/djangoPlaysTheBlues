from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from accounts.views import UserRegistrationView
from blog.views import NewBlogView, HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$',login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$',logout, {'next_page': '/login/'}, name='logout'),
    url(r'^blog/new/$', NewBlogView.as_view(), name='new-blog'),

]

