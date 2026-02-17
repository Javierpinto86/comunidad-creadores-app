from django.urls import path

from .views import checkout_placeholder_view

urlpatterns = [
    path("checkout/", checkout_placeholder_view, name="payments-checkout"),
]
