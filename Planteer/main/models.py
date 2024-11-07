from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    email = models.EmailField(max_length=254, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

