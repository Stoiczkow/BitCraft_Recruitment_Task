from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Links, Files
from .serializers import LinksSerializer, FilesSerializer
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView(views.View):
    def get(self, request):
        return render(request, 'base.html')


class CreateLink(CreateView, LoginRequiredMixin):
    model = Links
    fields = ['address']


class CreateFile(CreateView, LoginRequiredMixin):
    model = Files
    fields = ['file']


class LinkDetailView(DetailView, LoginRequiredMixin):
    model = Links


class GetLinkView(views.View, LoginRequiredMixin):
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


class FileDetailView(DetailView, LoginRequiredMixin):
    model = Files


class GetFileView(views.View, LoginRequiredMixin):
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


class StatsAPIView(APIView, LoginRequiredMixin):
    def get(self, request):
        result = {}
        links = Links.objects.filter(entries__gt=0)
        files = Files.objects.filter(entries__gt=0)

        for link in links:
            date = link.add_date.date().strftime("%Y-%m-%d")
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


class AddLinkAPIView(APIView, LoginRequiredMixin):
    """
    Needs fixes
    """

    def post(self, request, format=None):
        serializer = LinksSerializer(data=request.data)
        if serializer.is_valid():
            link = Links.objects.create(address=request.data['address'])
            link.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddFileAPIView(APIView, LoginRequiredMixin):
    """
    Needs fixes
    """

    def post(self, request, format=None):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            file = Files.objects.create(file=request.data['file'])
            file.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
