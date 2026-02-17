from django.contrib import admin

from .models import Delivery, DeliveryFile, Feedback, Project, WeeklyObjective


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "project_type", "phase", "status", "started_at")
    list_filter = ("project_type", "phase", "status", "band_level")
    search_fields = ("title", "user__username", "user__email")


@admin.register(WeeklyObjective)
class WeeklyObjectiveAdmin(admin.ModelAdmin):
    list_display = ("week_start_date", "created_by", "created_at")
    search_fields = ("objective_text",)


class DeliveryFileInline(admin.TabularInline):
    model = DeliveryFile
    extra = 0


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("project", "week_start_date", "status", "submitted_at")
    list_filter = ("status",)
    search_fields = ("project__title", "project__user__username")
    inlines = [DeliveryFileInline]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("delivery", "created_at")
    search_fields = ("delivery__project__title", "summary", "next_step")
