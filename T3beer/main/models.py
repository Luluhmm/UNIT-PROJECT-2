from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Mindfulness', 'Mindfulness'),
        ('Sleep', 'Sleep'),
        ('Anxiety', 'Anxiety'),
        ('Breathing', 'Breathing'),
    ]

    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    source = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Mindfulness')
    created_at = models.DateTimeField(auto_now_add=True)



class Game(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)