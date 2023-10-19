from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, views, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework_jwt.utils import jwt_response_payload_handler

from .models import Candidate, Interview, Feedback, SentEmail
from .serializers import CandidateSerializer, InterviewSerializer, FeedbackSerializer, SentEmailSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.mixins import UserPassesTestMixin
class CandidateViewSet(viewsets.ModelViewSet, JSONWebTokenAuthentication, UserPassesTestMixin, IsAuthenticated):
    def test_func(self):
        return self.request.user.groups.filter(name='interview_app.view_candidate').exists()
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class InterviewViewSet(viewsets.ModelViewSet, JSONWebTokenAuthentication, UserPassesTestMixin, IsAuthenticated):
    def test_func(self):
        return self.request.user.groups.filter(name='interview_app.view_interview').exists()
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class FeedbackViewSet(viewsets.ModelViewSet, JSONWebTokenAuthentication, UserPassesTestMixin, IsAuthenticated):
    def test_func(self):
        return self.request.user.groups.filter(name='interview_app.view_feedback').exists()
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ScheduledInterviewViewSet(viewsets.ModelViewSet, JSONWebTokenAuthentication, IsAuthenticated):
    queryset = Interview.objects.filter(status='Scheduled')
    serializer_class = InterviewSerializer

@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
@permission_classes([permissions.AllowAny,])
def get_sent_emails(request):
    if request.method == 'GET':
        queryset = SentEmail.objects.all()
        serializer = SentEmailSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        return Response(
            {"detail": "Method not allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

@api_view(['GET'])
@permission_classes([permissions.AllowAny,])
def home_apiview(request):
    if request.method == 'GET':
        return JsonResponse({"Message": "Please refer to /api/v1/swagger/schema/"})
    else:
        return Response(
            {"detail": "Method not allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )