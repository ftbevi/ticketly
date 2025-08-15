from django.urls import path

from .views.login import LoginPageView

urlpatterns = [
    path('login/', LoginPageView.as_view())
]
