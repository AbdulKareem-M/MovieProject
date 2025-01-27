from django.shortcuts import render

from django.views.generic import View

from movieapp.forms import MovieForm
from movieapp.models import MovieModel
# Create your views here.


class AddMovie(View):
  
  def get(self, request):
    
    form = MovieForm
    
    return render(request, 'addmovie.html', {'form':form})
  
  def post(self, request):
    
    form = MovieForm(request.POST)
    
    if form.is_valid():
      
      MovieModel.objects.create(**form.cleaned_data)
      
      return render(request, 'addmovie.html', {'form':form})
    