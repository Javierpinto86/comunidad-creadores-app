from django.contrib import admin
from django.urls import include, path
from membership.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('biblioteca/', include('library.urls')),
    path('', include('accounts.urls')),
    path('panel/', include('membership.urls')),
]
