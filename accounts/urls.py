from django.urls import path
from . import views

#accounts urls.py
urlpatterns = [
    path('signup/',views.CustomUserCreateView.as_view(),name='signup'),
]
