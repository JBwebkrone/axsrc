from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    """A form that creates a user, with no privileges, from the given username and password.
    """
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'dob', 'gender', 'phone', 'email')
        