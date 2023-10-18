from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Candidate, Interview, Feedback, CustomUser, SentEmail
from .validators_serializers import name_validator, phone_number_validator
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        email_exists = CustomUser.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': [name_validator, ]},
            'phone_number': {'validators': [phone_number_validator, ]}
        }

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class SentEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentEmail
        fields = '__all__'