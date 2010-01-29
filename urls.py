from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from basic.blog.models import Post
from staff.models import StaffMember

sitemaps = {
    'Flat Pages': FlatPageSitemap,
    'Blog Entries': GenericSitemap({
        'queryset': Post.objects.published(),
        'date_field': 'publish',
    }, priority=0.6),
    'Members': GenericSitemap({'queryset':StaffMember.objects.all()})
}

urlpatterns = patterns('',
    (r'^cache/', include('django_memcached.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('api.urls')),
    (r'^blog/', include('basic.blog.urls')),
    (r'^bio/', include('staff.urls')),
    (r'^contact/', include('contact_form.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^sitemap/$', 'django_ext.views.sitemap', {'sitemaps': sitemaps}),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'base.html', 'extra_context': {
        'object_list': lambda: Post.objects.published().order_by('-publish')[:5]
    }}),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
