import json

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import permissions

from InterviewSystem.interview_app.model_validators import name_validator, phone_number_validator
from InterviewSystem.interview_app.producers import candidate_producer

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45, null=True)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




class Candidate(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[name_validator,]
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=20,
        validators=[phone_number_validator, ]
    )
@receiver(post_save, sender=Candidate)
def send_message_for_new_candidate(sender, instance, **kwargs):
    if kwargs.get('created', False):
        candidate_producer.send(topic="Candidates",
                                value={"id": instance.id,
                                            "email": instance.email,
                                            "name": instance.name,
                                            'phone_number': instance.phone_number})
        candidate_producer.flush()


class CandidatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required permission for this view
        if view.action == 'create':
            # HR personnel can create candidates
            return request.user.has_perm('interview_app.create_candidate')
        elif view.action == 'retrieve':
            # Developers can view candidates
            return request.user.has_perm('interview_app.view_candidate')
        return False

class Interview(models.Model):
    STATUSES = (('Planned', 'Planned'), ('Scheduled', 'Scheduled'), ('Completed', 'Completed'))
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    interviewer = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='Planned'
    )


class Feedback(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=100)
    feedback_text = models.TextField()

@receiver(post_save, sender=Feedback)
def send_message_for_new_candidate(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # candidate_producer.send(topic="InterviewChange", value={"id": instance.id,
        #                         "interviewer": instance.interviewer,
        #                         "interview": instance.interview,
        #                         "feedback": instance.feedback_text})
        candidate_producer.send(topic="InterviewChange", value={"id": instance.id,
                                                                "interviewer": instance.interviewer,
                                                                "feedback_text": instance.feedback_text  })
        candidate_producer.flush()


class FeedbackPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the required permission for this view
        if view.action == 'create':
            # HR personnel can create candidates
            return request.user.has_perm('interview_app.create_candidate')
        elif view.action == 'retrieve':
            # Developers can view candidates
            return request.user.has_perm('interview_app.view_candidate')
        return False

class SentEmail(models.Model):
    sent_data = models.CharField(max_length=500)