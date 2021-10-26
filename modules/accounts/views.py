from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import Account
from .forms import RegistrationForm, PasswordResetForm

from django.contrib.auth.tokens import default_token_generator
from django.views.generic.edit import FormView
from .mixins import PasswordContextMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import gettext_lazy as _

class HomePageView(TemplateView):
    """
    HomePageView for homepage
    """
    template_name = "home.html"


class RegistrationView(CreateView):
    """Show the registration page and handle registration

    Returns:
        GET: Show the HTML page with `RegistrationForm`
        POST: Handle the `RegistrationForm`
    """
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        # if next_url:
        #     success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    """
    ProfileView for updating profile
    """
    model = Account
    fields = ['name', 'phone', 'date_of_birth', 'gender', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('home')

    def get_object(self):
        return self.request.user



class PasswordResetView(PasswordContextMixin, FormView):
    """
    PasswordResetView for reseting password and send email
    """
    email_template_name = 'registration/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = "jb.webkrone@gmail.com"
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    title = _('Password reset')
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        form_valid method for validating form
        """
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)


INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    """
    PasswordResetDoneView for handling the event after successfully reseting the password 
    """
    template_name = 'registration/password_reset_done.html'
    title = _('Password reset sent')