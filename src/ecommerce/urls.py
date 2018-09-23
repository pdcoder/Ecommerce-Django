from django.conf.urls import patterns, include, url
from .views import home_page, about_page, contact_page
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^ecommerce/', include('ecommerce.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$/', home_page),
    url(r'^$/about', about_page),
    url(r'^$/contact', contact_page),
    url(r'^admin/', include(admin.site.urls))
)
