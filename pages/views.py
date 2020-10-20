from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import CustomUser
from .forms import RecipeCreateForm
from django.urls import reverse, reverse_lazy
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
    # form_class = RecipeCreateForm
    model = Recipe
    fields = ["title","description","new_ingredients","instructions","prep_time","cook_time","food_pic"]
    template_name = "recipe_create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def recipe_favorite(request,slug):
    recipe = Recipe.objects.get(slug=slug)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)

    return reverse('recipe_detail', args=[recipe.slug])

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user == Recipe.objects.get(slug__iexact=self.kwargs.get("slug")).author
    model = Recipe
    fields = ['title','description','ingredients','prep_time','cook_time','instructions','food_pic']
    template_name = 'recipe_update.html'

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user == Recipe.objects.get(slug__iexact=self.kwargs.get("slug")).author
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipe_list')
