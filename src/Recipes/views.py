from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'Recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipes
    template_name = 'Recipes/recipelist.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'Recipes/recipedetail.html'