"""
acme_events project-level URL Configuration
"""
from .views import handler404, handler500
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('', include('events.urls')),
    path('', include('checkout.urls')),
    path('', include('cart.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'acme_events.views.handler404'
handler500 = 'acme_events.views.handler500'
