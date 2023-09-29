"""
URL configuration for sd_water_proofing_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view



schema_view = get_schema_view(
    openapi.Info(
        title="S.D WaterProofing API",
        default_version='v1',
        description="API for S.D WaterProofing",
        terms_of_service="https://www.sdwproofing.com/terms/",
        contact=openapi.Contact(email=settings.ADMIN_EMAIL),
        license=openapi.License(name="S.D WaterProofing License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("portfolio/", include("Portfolio.urls")),
    path("helpdesk/", include("helpdesk.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    