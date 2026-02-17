from django.urls import path

from .views import library_home_view

urlpatterns = [
    path('', library_home_view, name='library-home'),
]
