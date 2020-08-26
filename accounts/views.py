from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
# Create your views here.

class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm

    template_name = 'registration/signup.html'
