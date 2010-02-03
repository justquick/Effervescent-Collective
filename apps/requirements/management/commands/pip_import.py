from django.core.management.base import BaseCommand
from requirements.models import Requirement


class Command(BaseCommand):
    def handle(self, *files, **options):
        for f in files:
            for l in open(f).readlines():
                print Requirement.from_pip(l) or ''
