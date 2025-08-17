from django.shortcuts import render
from django.views.generic import TemplateView


class ResetPasswordPageView(TemplateView):
    template_name = "reset-password.html"

    def get(self, request):
        return render(request, self.template_name)
