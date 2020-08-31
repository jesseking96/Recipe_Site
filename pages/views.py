from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.contrib.auth import get_user_model
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
        myquery = self.request.GET.get('q')
        object_list = Recipe.objects.filter(Q(title__icontains=myquery) | Q(description__icontains=myquery))
        return object_list

class UserRecipeView(ListView):
    model = Recipe
    template_name = 'user_posts.html'

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(author__slug=self.kwargs.get("slug"))
