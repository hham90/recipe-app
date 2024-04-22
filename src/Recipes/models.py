from django.db import models

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField()
    cooking_time = models.FloatField()
    difficulty = models.TextField()

    def __str__(self):
        return str(self.name)