from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'vox_pop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$', 'home.views.main'),
    url(r'^admin/', include(admin.site.urls)),
    ]
