from django.contrib import admin
from django.urls import include, path
from core.views import home_view

admin.site.site_header = "Comunidad de Creadores Admin"
admin.site.site_title = "Comunidad de Creadores Admin"
admin.site.index_title = "Panel de gestion"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('biblioteca/', include('library.urls')),
    path('pagos/', include('payments.urls')),
    path('', include('accounts.urls')),
    path('panel/', include('program.urls')),
]
