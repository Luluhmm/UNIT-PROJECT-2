from django.db import models

# Create your models here.
class MoodEntry(models.Model):
    text = models.TextField()
    mood = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)