from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('converter/', include('Converter.urls')),  # Ensure the app name matches
    # Other URL patterns if any
]
