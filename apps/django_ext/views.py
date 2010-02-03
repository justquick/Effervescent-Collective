from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

clean = lambda i: '/'+'/'.join(i['location'].split('/')[3:])

def sitemap(request, sitemaps):
    maps = {}
    for section, site in sitemaps.items():
        if callable(site):
            maps[section] = map(clean, site().get_urls())
        else:
            maps[section] = map(clean, site.get_urls())
    return render_to_response('sitemap.html',{'maps':maps},
            context_instance=RequestContext(request))
    
def feed(request, **kwargs):
    return render_to_response('feed.xml', kwargs, mimetype='application/rss+xml',context_instance=RequestContext(request))