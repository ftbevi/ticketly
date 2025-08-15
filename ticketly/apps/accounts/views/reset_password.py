from django.shortcuts import render
from django.views.generic import TemplateView

from apps.accounts.forms import AuthenticationForm


class ResetPasswordPageView(TemplateView):
    template_name = "reset-password.html"

    def get(self, request):
        return render(request, self.template_name)
