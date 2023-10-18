
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, authentication
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

the_schema_view = get_schema_view(
    openapi.Info(
        title="Api Docs",
        default_version='1.0.0',
        description="Documentation of the API"
    ),
    permission_classes=[permissions.AllowAny,],
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("InterviewSystem.interview_app.urls")),
    path('api/v1/', include([
        path('swagger/schema/', the_schema_view().with_ui('swagger', cache_timeout=0), name="swagger-schema")
    ]))


]
