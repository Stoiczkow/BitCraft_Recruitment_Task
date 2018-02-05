from django.shortcuts import render
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Links, Files
# Create your views here.

class HomeView(views.View):
    def get(self, request):
        return render(request, 'base.html')


class CreateLink(CreateView):
    model = Links
    fields = ['address']
