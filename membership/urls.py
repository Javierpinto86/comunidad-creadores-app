from django.urls import path

from .views import member_area_view, panel_view, restricted_access_view

urlpatterns = [
    path('', panel_view, name='panel'),
    path('membresia/', member_area_view, name='member-area'),
    path('acceso-restringido/', restricted_access_view, name='restricted-access'),
]
