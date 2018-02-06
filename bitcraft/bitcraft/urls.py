"""bitcraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from protected_links.views import (HomeView, CreateLink, CreateFile,
                                   LinkDetailView, GetLinkView, FileDetailView,
                                   GetFileView, StatsAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', HomeView.as_view()),
    path('add_link/', CreateLink.as_view(), name='add_link'),
    path('add_file/', CreateFile.as_view(), name='add_file'),
    path('link/<pk>/', LinkDetailView.as_view()),
    path('get_link/<token>/', GetLinkView.as_view()),
    path('file/<pk>/', FileDetailView.as_view()),
    path('get_file/<token>/', GetFileView.as_view()),
    path('api/stats/', StatsAPIView.as_view()),
]
