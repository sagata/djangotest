from django.conf.urls import patterns, include, url
from testapp.views import hello
from testapp.views import hello2
from testapp.views import search_form
from testapp.views import search
from testapp.views import contact_form
from testapp.views import contact
from testapp.views import thanks,current_datetime
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    (r'^hello/\d{1,2}/$', hello2),
    (r'^search‐form/$', search_form),
    (r'^search/$', search),
    (r'^contact-form/$', contact_form ),
    (r'^contact/$', contact ),
    (r'^thanks/$', thanks ),
    (r'^current_datetime/$', current_datetime ),
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^djangotest/', include('djangotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
