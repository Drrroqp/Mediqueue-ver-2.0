from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'mq/index.html')


def registration(request):
    return render(request, 'mq/profile.html')