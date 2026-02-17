from django.shortcuts import render


def checkout_placeholder_view(request):
    return render(request, "payments/checkout_placeholder.html")
