from django.shortcuts import render
from django.views import generic
from django.middleware.csrf import rotate_token


class HomeView(generic.View):
    template_name = "home/home.html"

    def get(self, *args, **kwargs):
        rotate_token(self.request)
        return render(self.request, self.template_name)