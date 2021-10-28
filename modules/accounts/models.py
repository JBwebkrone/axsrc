from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django import utils
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse


class AccountManager(BaseUserManager):
    """
    Account manager for Account model
    """
    use_in_migrations = True

    def _create_user(self, email, first_name, phone, password, **extra_fields):
        values = [email, first_name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, phone, password=None, **extra_fields):
        """
        Creating user
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, phone, password, **extra_fields)

    def create_superuser(self, email, first_name, phone, password=None, **extra_fields):
        """
        Creating super user
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, phone, password, **extra_fields)

GENDER = (
    ('m', 'male'),
    ('f', 'female'),
)
class Account(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model, using AbstractBaseUser
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=GENDER, default='m')
    # date_of_birth = models.DateField(blank=True, null=True, default="1999/09/20")
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone']

    def __str__(self):
        return self.first_name

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_password_reset_url(self):
        """
        Generating password reset URL 
        """
        base64_encoded_id = utils.http.urlsafe_base64_encode(utils.encoding.force_bytes(self.id))
        token = PasswordResetTokenGenerator().make_token(self)
        reset_url_args = {'uidb64': base64_encoded_id, 'token': token}
        reset_path = reverse('password_reset_confirm', kwargs=reset_url_args)
        reset_url = f'{settings.BASE_URL}{reset_path}'
        return reset_url
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_joined"]