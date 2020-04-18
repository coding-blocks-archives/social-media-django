from django.urls import path

from social import views

urlpatterns = [
  path('home/', views.Home.as_view()),
  path('', views.Wall.as_view())
]
