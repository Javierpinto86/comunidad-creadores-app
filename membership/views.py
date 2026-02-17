from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .decorators import active_member_required


def home_view(request):
    return render(request, 'home.html')


@login_required
def panel_view(request):
    return render(request, 'membership/panel.html')


@active_member_required
def member_area_view(request):
    return render(request, "membership/member_area.html")


def restricted_access_view(request):
    return render(request, "membership/restricted_access.html")
