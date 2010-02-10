from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.flatpages.models import FlatPage
from basic.blog.models import Post
from staff.models import StaffMember
from django.contrib.syndication.feeds import Feed

class LatestEntriesFeed(Feed):
    title = "Chicagocrime.org site news"
    link = "/blog/feed/"
    description = "Updates on changes and additions to chicagocrime.org."

    def items(self):
        return Post.objects.published.order_by('-publish')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
    
    def item_pubdate(self, obj):
        return obj.publish

sitemaps = {
    'Pages': FlatPageSitemap,
    'Blog Entries': GenericSitemap({
        'queryset': Post.objects.published(),
        'date_field': 'publish',
    }, priority=0.6),
    'Members': GenericSitemap({'queryset':StaffMember.objects.all()})
}

from contact_form.forms import ContactForm
from math_captcha.forms import MathCaptchaForm

class CaptchaContactForm(ContactForm,MathCaptchaForm):
    pass

urlpatterns = patterns('',
    (r'^cache/', include('django_memcached.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('api.urls')),
    (r'^frontendadmin/', include('frontendadmin.urls')),
    (r'^blog/', include('basic.blog.urls')),
    url(r'^terminal/', 'terminal.views.terminal', name='terminal'),
    (r'^comments/', include('mptt_comments.urls')),
    (r'^bio/', include('staff.urls')),
    url(r'^contact/$','contact_form.views.contact_form',{'form_class':CaptchaContactForm},name='contact_form'),
    url(r'^contact/sent/$','django.views.generic.simple.direct_to_template',{ 'template': 'contact_form/contact_form_sent.html' },name='contact_form_sent'),    
    url(r'^feeds/blog/$', 'django_ext.views.feed', {
        'items': Post.objects.published().order_by('-publish')[:10],
        'title': 'Recent blog entries',
    }, name='blog_feed'),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^sitemap/$', 'django_ext.views.sitemap', {'sitemaps': sitemaps}),
    (r'^search/$', 'django.views.generic.simple.direct_to_template', {'template':'search.html'}),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'base.html', 'extra_context': {
        'object_list': lambda: Post.objects.published().order_by('-publish')[:5],
        'flatpages': lambda: FlatPage.objects.all()[:1]
    }}),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
