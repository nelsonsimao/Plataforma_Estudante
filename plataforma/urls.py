#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from plataforma import settings, views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plataforma.views.home', name='home'),
    # url(r'^plataforma/', include('plataforma.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^carpool/', include('carpool.urls')),
    url(r'^alojamentos/', include('alojamentos.urls')),
    
    #url(r'^accounts/', include('registration.urls')),
    #url(r'^accounts/profile', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^$', TemplateView.as_view(template_name='login_page.html'), name='index_base'),
    
    url(r'^menu/', views.menu, name='menu'),
)
