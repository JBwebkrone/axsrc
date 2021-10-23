from django.urls import path
from .views import (
    SignupView,
    LoginCreateView,
)

urlpatterns = [
    path('login/', LoginCreateView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
]