from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    (r'^pets/', include('project.pets.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
    )
try:
    urlpatterns += patterns('',
        (r'^log/emails/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.EMAIL_FILE_PATH, 'show_indexes': True}),
    )
except AttributeError:
    pass