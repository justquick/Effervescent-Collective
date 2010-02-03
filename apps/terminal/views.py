from django.http import HttpResponse
from subprocess import Popen, PIPE
from shlex import split
from cStringIO import StringIO

def handler(input):
    args = [filter(lambda c: c != '\x00', i) for i in split(input)]
    
    try:
        return HttpResponse(Popen(args, stdout=PIPE).communicate()[0])
    except Exception, e:
        return 'SERVER ERROR: %s' % e
    
    
def terminal(request):
    if not request.user.is_superuser:
        return HttpResponse('Not authorized')
    return HttpResponse(handler(request.POST.get('input',None)) or '')