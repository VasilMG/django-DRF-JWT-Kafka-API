from django.contrib.auth.models import Group

# Create the HR group
hr_group, created = Group.objects.get_or_create(name='HR')

# Create the Interviewer group
interviewer_group, created1 = Group.objects.get_or_create(name='Interviewer')

hr_group.permissions.add(
    'interview_app.add_candidate',
    'interview_app.change_candidate',
    'interview_app.delete_candidate',
    'interview_app.view_candidate',
    'interview_app.view_interview',
    'interview_app.delete_interview',
    'interview_app.change_interview',
    'interview_app.add_interview',
)

interviewer_group.permissions.add(
    'interview_app.view_interview',
    'interview_app.delete_interview',
    'interview_app.change_interview',
    'interview_app.add_interview',
    'interview_app.add_feedback',
    'interview_app.change_feedback',
    'interview_app.delete_feedback',
    'interview_app.view_feedback',
    'interview_app.view_candidate',
)