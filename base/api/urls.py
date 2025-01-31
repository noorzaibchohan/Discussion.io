from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views  # Import API views

# Swagger schema configuration
schema_view = get_schema_view(
    openapi.Info(
        title="StudyBud API",
        default_version='v1',
        description="API documentation for the StudyBud project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@studybud.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# API URL patterns
urlpatterns = [
    # API Endpoints
    path('', views.getRoutes, name='api-routes'),
    path('rooms/', views.getRooms, name='room-list'),
    path('rooms/<str:pk>/', views.getRoom, name='room-detail'),

    # Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Optional ReDoc UI
]
