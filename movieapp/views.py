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
    
class ListMovies(View):
  
  def get(self, request):
    
    data = MovieModel.objects.all()
    
    return render(request, 'movies.html', {'data':data})

class UpdateMovie(View):
  
  def get(self, request, **kwargs):
    
    id = kwargs.get('pk')
    
    data = MovieModel.objects.get(id=id)
    
    form = MovieForm(instance=data)
    
    return render(request, 'updatemovie.html',{'form':form})
  
  
  def post(self, request, **kwargs):
    
    id = kwargs.get('pk')
    
    data = MovieModel.objects.get(id=id)
    
    form = MovieForm(request.POST, instance=data)
    
    if form.is_valid():
      
      form.save()
      
    return render(request, 'updatemovie.html', {'form':form})
  
class DeleteMovie(View):
  
  def get(self, request, **kwargs):
    
    id = kwargs.get('pk')
    
    MovieModel.objects.get(id=id).delete()
    
    return render(request,'delete.html')  