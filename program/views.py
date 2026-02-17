from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .decorators import active_subscription_required
from .models import Project, WeeklyObjective


@active_subscription_required
def dashboard_view(request):
    project = Project.objects.filter(user=request.user).first()
    weekly_objective = WeeklyObjective.objects.first()
    return render(
        request,
        "program/dashboard.html",
        {
            "project": project,
            "weekly_objective": weekly_objective,
        },
    )


@login_required
def restricted_access_view(request):
    return render(request, "program/restricted_access.html")
