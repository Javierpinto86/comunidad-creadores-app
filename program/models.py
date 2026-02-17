from django.conf import settings
from django.db import models


class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ("original", "Original"),
        ("adaptacion", "Adaptacion"),
        ("arreglo", "Arreglo"),
    ]
    BAND_LEVEL_CHOICES = [
        ("juvenil", "Juvenil"),
        ("profesional", "Profesional"),
        ("superior", "Superior"),
        ("otro", "Otro"),
    ]
    PHASE_CHOICES = [
        ("design", "Design"),
        ("develop", "Develop"),
        ("orchestrate", "Orchestrate"),
        ("edit", "Edit"),
    ]
    STATUS_CHOICES = [
        ("active", "Active"),
        ("paused", "Paused"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
    band_level = models.CharField(max_length=20, choices=BAND_LEVEL_CHOICES, default="otro")
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES, default="design")
    current_milestone = models.TextField(blank=True)
    next_milestone = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    started_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class WeeklyObjective(models.Model):
    week_start_date = models.DateField(unique=True)
    objective_text = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="weekly_objectives"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-week_start_date"]

    def __str__(self):
        return f"Objetivo semana {self.week_start_date}"


class Delivery(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="deliveries")
    week_start_date = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    student_notes = models.TextField(blank=True)
    objective_worked = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"Entrega {self.project.title} - {self.week_start_date}"


class DeliveryFile(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name="files")
    file_url = models.URLField(max_length=500)
    file_type = models.CharField(max_length=50, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"Archivo {self.file_type or 'adjunto'}"


class Feedback(models.Model):
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, related_name="feedback")
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    audio_url = models.URLField(max_length=500, blank=True)
    next_step = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Feedback {self.delivery.project.title}"
