from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now=True)
  content = models.TextField()
  image = models.ImageField(blank = True)

  def __str__(self):
    return self.content[:50]

class Friends(models.Model):
  person1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person1')
  person2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person2')
