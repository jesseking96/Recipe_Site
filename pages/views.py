from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic import DetailView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
