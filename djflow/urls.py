from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from djflow.core.json_settings import get_settings

settings_json = get_settings()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('flow/', include('flow.urls')),
    path('security/', include('security.urls'))
]

if settings_json["DEBUG"]:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
