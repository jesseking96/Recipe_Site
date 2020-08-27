from django.urls import path
from . import views
#pages urls.py
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('recipes/',views.RecipeListView.as_view(),name='recipe_list'),
    path('recipes/<int:pk>',views.RecipeDetailView.as_view(),name='recipe_detail'),
    path('search/',views.SearchResultsView.as_view(),name='search_results'),
]
