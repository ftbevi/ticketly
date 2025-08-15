from django.urls import path

from .views.login import LoginPageView
from .views.reset_password import ResetPasswordPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('reset-password/', ResetPasswordPageView.as_view(), name='reset_password')
]
