from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^real/$', 'BK.views.hello', name='real'),
    url(r'^display/$', 'BK.views.search', name='search'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', 'BK.views.login',name='login'),
    # url(r'^auth/$', 'BK.views.auth'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$','BK.views.logout'),
    # url(r'^accounts/logout/$', auth_views.logout),
    url(
    regex=r'^login/$', 
    view=login, 
    kwargs={'template_name': 'login.html'}, 
    name='login'
),
     # url(r'^accounts/logout/$', auth_views.logout),
url(
    regex=r'^logout/$', 
    view=logout, 
    kwargs={'next_page': '/'}, 
    name='logout'
),
 url(r'^connection/$','BK.views.formView', name = 'loginform'),
   url(r'^login/', 'login', name = 'login'),
   


)
