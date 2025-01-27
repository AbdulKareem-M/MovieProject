from movieapp.models import MovieModel
from django import forms

class MovieForm(forms.ModelForm):
  
  class Meta:
    
    model = MovieModel
    
    fields = '__all__'