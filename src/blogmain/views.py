from django.http import HttpResponse
from django.shortcuts import render

# def home_page(request):
#     return HttpResponse("Hello world")

def home_page(request):
    return render(request, "index.html")

def aboutus_page(request):
    return render(request, "aboutus.html")