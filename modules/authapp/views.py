from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import FormView
from .forms import (
    SignupForm,
)

print(settings.STATICFILE_DIRS)

class SignupView(FormView):
    template_name = "registration/signup.html"
    form_class = SignupForm