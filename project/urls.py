from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    (r'^pets/', include('project.pets.urls')),
    (r'^admin/', include(admin.site.urls)),
)
