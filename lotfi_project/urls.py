from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_panel.urls')), 
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
