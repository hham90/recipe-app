from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes

# Create your views here.
def home(request):
    return render(request, 'Recipes/home.html')

class RecipeListView(ListView):
    model = Recipes
    template_name = 'Recipes/recipelist.html'

class RecipeDetailView(DetailView):
    model = Recipes
    template_name = 'Recipes/recipedetail.html'