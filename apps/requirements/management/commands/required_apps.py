from django.core.management.base import BaseCommand
from requirements.models import Requirement

class Command(BaseCommand):
    def handle(self, *args, **options):
        print 'INSTALLED_APPS += ('
        for req in Requirement.objects.all():
            if not req.egg in (None,'django'):
                print "    '%s'," % req.egg
        print ')'
