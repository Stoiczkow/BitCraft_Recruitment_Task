from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Links, Files
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
import json

# Create your views here.

class HomeView(views.View):
    def get(self, request):
        return render(request, 'base.html')


class CreateLink(CreateView):
    model = Links
    fields = ['address']


class CreateFile(CreateView):
    model = Files
    fields = ['file']


class LinkDetailView(DetailView):
    model = Links


class GetLinkView(views.View):
    def get(self, request, token):
        return render(request, 'get_link.html')

    def post(self, request, token):
        link = Links.objects.get(token=token)

        if datetime.datetime.now(
                datetime.timezone.utc) - link.add_date > datetime.timedelta(1):
            link.is_active = False
            link.save()
            return render(request, 'expired.html')

        if request.POST['password'] == link.password:
            link.entries += 1
            link.user_agent = request.META['HTTP_USER_AGENT']
            link.save()
            return redirect('{}'.format(link.address))
        else:
            return render(request, 'invalid_pass.html')


class FileDetailView(DetailView):
    model = Files


class GetFileView(views.View):
    def get(self, request, token):
        return render(request, 'get_file.html')

    def post(self, request, token):
        file_to_dl = Files.objects.get(token=token)

        if datetime.datetime.now(
                datetime.timezone.utc) - file_to_dl.add_date > datetime.timedelta(
                1):
            file_to_dl.is_active = False
            file_to_dl.save()
            return render(request, 'expired.html')

        if request.POST['password'] == file_to_dl.password:
            file_to_dl.entries += 1
            file_to_dl.user_agent = request.META['HTTP_USER_AGENT']
            file_to_dl.save()
            file_to_dl = file_to_dl.file.name.split('/')[-1]
            response = HttpResponse(file_to_dl.file,
                                    content_type='text/plain')
            response[
                'Content-Disposition'] = 'attachment; filename=%s' % file_to_dl

            return response
        else:
            return render(request, 'invalid_pass.html')


class StatsAPIView(APIView):
    """
    Date in format RRRR-MM-DD.
    """
    def get(self, request):
        result = {}
        links = Links.objects.filter(entries__gt=0)
        files = Files.objects.filter(entries__gt=0)

        for link in links:
            date = link.add_date.date().strftime("%Y-%m-%d")
            print(date)
            if date in result:
                result[date]["links"] += 1
            else:
                result[date] = {"links": 1,
                                "files": 0}

        for file in files:
            date = file.add_date.date().strftime("%Y-%m-%d")
            if date in result:
                result[date]["files"] += 1
            else:
                result[date] = {"links": 0,
                                "files": 1}

        return Response(result)