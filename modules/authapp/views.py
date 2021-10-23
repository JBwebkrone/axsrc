from django.urls import reverse_lazy
from django.conf import settings
from django.urls.base import reverse
from django.views.generic.edit import CreateView
from .forms import (
    CustomUserCreationForm,
)



class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    