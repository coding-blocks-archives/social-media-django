from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from social import models

# Create your views here.
class Wall(LoginRequiredMixin, ListView):
  queryset = models.Post.objects.all()
  context_object_name = 'posts'
  template_name = 'social/wall.html'
  login_url = 'auth/login'

