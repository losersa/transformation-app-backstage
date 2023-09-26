# -*- coding: UTF-8 -*- #
"""
@filename:urls.py
@author:Gxr
@time:2023-09-14
djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from djangoProject import settings
from my_app import views

urlpatterns = [
    path('', views.index),
    path('upload/', views.upload_files.as_view()),
    # path('pdf2img/', views.pdftopil.as_view(), name='pdf2img'),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


