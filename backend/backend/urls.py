from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/products/', include('apps.products.urls')),
]

if settings.DEBUG:
    # Static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Swagger
    urlpatterns += [
        path('schema/raw/', SpectacularAPIView.as_view(), name='schema'),
        path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger')
    ]
