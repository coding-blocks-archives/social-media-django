from django.shortcuts import render
from django.views.generic import ListView

from social import models

# Create your views here.
class Wall(ListView):
  queryset = models.Post.objects.all()
  context_object_name = 'posts'
  template_name = 'social/wall.html'

