from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import (
    SignupForm,
)

class SignupView(FormView):
    template_name = "registration/signup.html"
    form_class = SignupForm