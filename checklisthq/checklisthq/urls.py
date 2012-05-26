from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^users/new$', 'main.views.new_user', name="new_user"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^.*$', 'main.views.home', name='home'),
    # url(r'^checklisthq/', include('checklisthq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
