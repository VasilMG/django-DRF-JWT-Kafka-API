from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from InterviewSystem.interview_app.models import CustomUser
from django.contrib.auth.models import Group
class Command(BaseCommand):

    def handle(self, *args, **options):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        group_hr, created_hr = Group.objects.get_or_create(name='HR')
        hruser.groups.add(group_hr)

        dev_user = CustomUser.objects.create(
            email="dev@dev.com",
            first_name="Dev",
            last_name="Person",
            password=make_password('devperson.123'),
        )
        group_dev, created_dev = Group.objects.get_or_create(name='Interviewer')
        dev_user.groups.add(group_dev)
