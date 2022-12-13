from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('project_watches.web.urls')),
    path('auth/', include('project_watches.auth_app.urls')),
    path('api/', include('project_watches.api.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'project_watches.web.views.custom_404_error'
