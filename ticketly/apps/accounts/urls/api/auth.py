from django.urls import path

from apps.accounts.views.api.auth import (
    TokenObtainPairViewCustom,
    TokenRefreshViewCustom,
    LogoutView,
    ForgotPasswordView,
    ResetPasswordConfirmView,
    MeView
)


urlpatterns = [
    path("token/", TokenObtainPairViewCustom.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshViewCustom.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("reset-password-confirm/", ResetPasswordConfirmView.as_view(), name="reset_password_confirm"),
    path("me/", MeView.as_view(), name="me"),
]
