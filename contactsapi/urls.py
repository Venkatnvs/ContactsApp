from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from contacts.views import ReverseString,video_p2p,video_p2p_room

schema_view = get_schema_view(
    openapi.Info(
        title="Contacts List API",
        default_version='v1',
        description="An API for contacts",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('client.urls')),
    path('api/contacts/',include('contacts.urls')),
    path('api/str-rev/',ReverseString),
    path('call/',video_p2p_room,name='call_room'),
    path('room/',video_p2p,name="call_i"),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
