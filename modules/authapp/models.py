<<<<<<< HEAD
=======
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


GENDER = (
    ('m', 'male'),
    ('f', 'female'),
)

class CustomUser(AbstractUser):

    """Custom user model for creating users
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)

    dob = models.DateField(
        _("Date of birth"),
    )

    gender = models.CharField(
        max_length=2,
        choices=GENDER,
    )

    phone = models.IntegerField(
        _("Phone number"),
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name
>>>>>>> b7518fbe365aee572bca4196084771f764a6b268
