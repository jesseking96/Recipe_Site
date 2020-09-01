from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import CustomUser
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['featured'] = Recipe.objects.filter(featured__exact=True)
        context['recent_five']=Recipe.objects.order_by("created_date")[:5]
        return context

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

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_author'] = CustomUser.objects.get(slug__exact=self.kwargs.get("slug"))
        return context

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["title","description","ingredients","instructions","prep_time","cook_time","food_pic"]
    template_name = "recipe_create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
