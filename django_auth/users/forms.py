from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    # cover Meta, change to 'users.User'
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
