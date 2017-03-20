from django import forms

from .models import restaurants


class RestaurantesForm(forms.Form):
  name = forms.CharField(required=True, max_length=80)
  cuisine = forms.CharField()
  borough = forms.CharField(widget=forms.TextInput())
