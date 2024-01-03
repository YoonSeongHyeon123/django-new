from django import forms
from .models import communicate
class CreateForm(forms.ModelForm):
  class Meta:
    model = communicate
    fields = ['title', 'pub_date', 'body']