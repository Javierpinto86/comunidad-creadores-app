from django.contrib import admin

from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "current_period_end", "last_event_at")
    list_filter = ("status",)
    search_fields = ("user__username", "user__email", "stripe_customer_id", "stripe_subscription_id")
