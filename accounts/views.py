from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from pages.models import Recipe
from .models import CustomUser
from django.urls import reverse_lazy
# Create your views here.

class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm

    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'
