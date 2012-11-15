from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from resultat import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zozaniba.views.home', name='home'),
    # url(r'^zozaniba/', include('zozaniba.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^$', views.home, name="home"),
    url(r'^diabili/(?:(?P<answer>))$', views.diabili, name="diabili"),
    # url(r'^diabili/answer/(?:(?P<answer>))$', views.answer, name="answer"),
    url(r'^diabili/getask/$', views.getask, name="getask"),
    url(r'^about/$', direct_to_template, {'template': 'about.html'},
                                                                 name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
