from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('schema/raw/', SpectacularAPIView.as_view(), name='schema'),
        path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger')
    ]
