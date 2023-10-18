# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, InterviewViewSet, FeedbackViewSet, ScheduledInterviewViewSet,get_sent_emails, home_apiview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet, basename='candidates')
router.register(r'interviews', InterviewViewSet, basename='interviews')
router.register(r'feedback', FeedbackViewSet, basename='feedbacks')
router.register(r'schedule', ScheduledInterviewViewSet, basename='scheduled-interviews')

urlpatterns = [
    path('access/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
    path('api/', include(router.urls)),
    path('api/emails/', get_sent_emails, name="get-emails"),
    path('', home_apiview, name='main-url')
]
