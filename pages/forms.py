from django import forms
from .models import Recipe
from django.contrib.postgres.forms import SimpleArrayField

class RecipeCreateForm(forms.ModelForm):
    ingred = SimpleArrayField(forms.CharField(),delimiter=',')
    class Meta:
        model = Recipe
        fields = ["title","description","instructions","prep_time","cook_time","food_pic"]

    def is_valid(self):
        self.author = self.request.user
        super().clean()
