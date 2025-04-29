from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATE_CHOICES = [
        ("running", "Running"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default="running")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.state})"
