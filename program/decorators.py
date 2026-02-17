from functools import wraps

from django.shortcuts import redirect


def active_subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect("login")
        if user.is_staff:
            return view_func(request, *args, **kwargs)

        subscription = getattr(user, "subscription", None)
        if not subscription or subscription.status not in {"active", "trialing"}:
            return redirect("restricted-access")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
