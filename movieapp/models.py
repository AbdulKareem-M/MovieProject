from django.db import models

class MovieModel(models.Model):
  
  name = models.CharField(max_length=100)
  
  language = models.CharField(max_length=100)
  
  director = models.CharField(max_length=100)
  
  year = models.PositiveIntegerField()
  
  runtime_in_minutes = models.PositiveIntegerField()
  
  
  