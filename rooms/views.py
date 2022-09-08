from django.shortcuts import render
from django.http import HttpResponse


def all_rooms(request):
    print(request)
    return HttpResponse(content="Hello")
