from django.contrib import admin
from django.urls import include, path

from api.router import router as api_router

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
]
