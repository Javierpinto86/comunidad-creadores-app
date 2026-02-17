from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


@login_required
def panel_view(request):
    return render(request, 'membership/panel.html')
