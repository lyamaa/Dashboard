from django.shortcuts import render


def index(request):
    return render(request, template_name="index.html")


from django.conf import settings

from django.views.generic.base import TemplateView


class IndexTemplateView(TemplateView):
    def get_template_names(self):
        return "index.html"
