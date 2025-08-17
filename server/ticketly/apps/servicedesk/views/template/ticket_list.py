from django.shortcuts import render
from django.views.generic import TemplateView


class TicketListPageView(TemplateView):
    template_name = "ticket/list.html"

    def get(self, request):
        return render(request, self.template_name)
