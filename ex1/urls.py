from django.contrib import admin
from django.urls import path, include  # include is required to link app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for admin panel
    path('', include('ex1app.urls')),  # Includes the URLs from ex1app
]
