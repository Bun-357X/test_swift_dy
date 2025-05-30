"""
URL configuration for exam_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import SchoolViewSet, ClassroomViewSet, TeacherViewSet, ClassroomTeacherViewSet, StudentViewSet

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('school', SchoolViewSet)
router.register('classroom', ClassroomViewSet)
router.register('teacher', TeacherViewSet)
router.register('classroom_teacher', ClassroomTeacherViewSet)
router.register('student', StudentViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="API documentation with Swagger UI",
      terms_of_service="^_^",
      contact=openapi.Contact(email="you@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('apis.urls')),
    path('api/', include(router.urls)),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
