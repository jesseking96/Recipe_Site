from django.urls import path
from . import views
#pages urls.py
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('recipes/',views.RecipeListView.as_view(),name='recipe_list'),
    path('recipes/<slug:slug>',views.RecipeDetailView.as_view(),name='recipe_detail'),
    path('search/',views.SearchResultsView.as_view(),name='search_results'),
    path('recipes/by_user/<slug:slug>',views.UserRecipeView.as_view(),name='user_recipes'),
    path('recipes/edit/create',views.RecipeCreateView.as_view(),name="recipe_create"),
]
