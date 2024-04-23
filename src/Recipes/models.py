from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField()
    cooking_time = models.FloatField()
    difficulty = models.TextField()
    pic = models.ImageField(upload_to='Recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse ( 'Recipes:recipedetail', kwargs={'pk': self.pk})