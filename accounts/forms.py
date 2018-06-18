from django.forms import ModelForm
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password',]
