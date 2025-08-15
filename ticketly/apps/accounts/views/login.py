from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.http import JsonResponse

from apps.accounts.forms import AuthenticationForm


class LoginPageView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"success": True, "redirect_url": "/tickets/"})

        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
