from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
# Create your views here.

class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm

    template_name = 'registration/signup.html'

class UserProfileView(DetailView):
    model = get_user_model()
    template_name = 'user_profile.html'
