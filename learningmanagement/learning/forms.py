from django.contrib.auth.forms import UserCreationForm
from .models import instructorModel
from django.contrib.auth.models import User

class Instructorform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class Studentform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
