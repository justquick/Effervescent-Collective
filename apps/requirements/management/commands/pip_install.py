from django.core.management.base import BaseCommand
from requirements.models import Requirement
from subprocess import check_call

class Command(BaseCommand):
    def handle(self, *args, **options): 
        for req in Requirement.objects.all():
            check_call(['pip','install'] + list(req.to_pip()))
