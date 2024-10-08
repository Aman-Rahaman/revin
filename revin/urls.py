
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('admin_dashboard.urls')),
    path('', include('admin_dashboard.urls')),
]
