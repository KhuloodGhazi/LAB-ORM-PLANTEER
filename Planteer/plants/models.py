from django.db import models
from django.utils import timezone

# Create your models here.

class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = 'TECH', 'Technology'
        BUSINESS = 'BUS', 'Business'
        LIFESTYLE = 'LIFE', 'Lifestyle'
        EDUCATION = 'EDU', 'Education'
        HEALTH = 'HEALTH', 'Health'
        ENTERTAINMENT = 'ENT', 'Entertainment'

    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="blog_photos/", default="blog_photos/code.jpg")
    is_edible = models.BooleanField(default=True) #search more(choies)
    create_at = models.DateTimeField(auto_now_add=True) #search more
    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TECHNOLOGY
    )

