from django.shortcuts import render
from django.views.generic import TemplateView

from apps.accounts.forms import AuthenticationForm


class LoginPageView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
