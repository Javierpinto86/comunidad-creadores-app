from django.urls import path

from .views import dashboard_view, restricted_access_view

urlpatterns = [
    path("", dashboard_view, name="panel"),
    path("acceso-restringido/", restricted_access_view, name="restricted-access"),
]
