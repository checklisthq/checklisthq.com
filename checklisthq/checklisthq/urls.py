from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^users/new$', 'main.views.new_user', name="new_user"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^settings$', 'django.contrib.auth.views.password_change'),
    url(r'^done$', 'django.contrib.auth.views.password_change_done'),
    url(r'^user/(?P<username>[a-zA-Z0-9_]+)$', 'main.views.checklist_list',
        name="checklist_list"),
    url(r'^checklist/new$', 'main.views.new_checklist', name='new_checklist'),
    url(r'^checklist/(?P<id>[0-9]+)$', 'main.views.view_checklist', name='view_checklist'),
    url(r'^checklist/(?P<id>[0-9]+)/edit$', 'main.views.edit_checklist', name='edit_checklist'),
    url(r'^.*$', 'main.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^.*$', 'main.views.home', name='home'),
)
