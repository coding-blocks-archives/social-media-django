from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class Login(LoginView):
  template_name = 'auth/login.html'

class Logout(LogoutView):
  pass
