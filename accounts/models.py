from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    is_active_member = models.BooleanField(default=False)
