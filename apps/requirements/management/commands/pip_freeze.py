from django.core.management.base import BaseCommand
from requirements.models import Requirement


class Command(BaseCommand):
    """
    Output all currently installed packages (exact versions) to stdout
    """
    def handle(self, *args, **options):
        for req in Requirement.objects.all():
            print req.pip
