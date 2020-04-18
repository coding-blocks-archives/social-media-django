from django.urls import path

from social import views

urlpatterns = [
  path('', views.Wall.as_view())
]
