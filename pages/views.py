from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class SearchResultsView(ListView):
    model = Recipe
    template_name='recipe_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Recipe.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return object_list
