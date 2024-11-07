from django.db import models
from django.utils import timezone

# Create your models here.

class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        FLOWER = 'Flower', 'Flower'
        TREE = 'Tree', 'Tree'
        SHRUB = 'Shrub', 'Shrub'
        HERB = 'Herb', 'Herb'
        VEGETABLE = 'Vegetable', 'Vegetable'
        FRUIT = 'Fruit', 'Fruit'

    name = models.CharField(max_length=1024) #
    about = models.TextField() #
    used_for = models.TextField() #
    image = models.ImageField(upload_to="images/", default="") #
    native_locations = models.CharField(max_length=200) #
    is_edible = models.BooleanField(default=False) #search more(choies)
    create_at = models.DateTimeField(auto_now_add=True) #search more
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
    )

