from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from .yasg import info


schema_view = get_schema_view(
    info,
    public=True,
    permission_classes=[AllowAny],
)

API_PREFIX = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/', include('cv_data.urls')),
]

urlpatterns += [
    path('swagger<str:format>/', schema_view.without_ui(), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
    # re_path(r".*", TemplateView.as_view(template_name="index.html")),
]
