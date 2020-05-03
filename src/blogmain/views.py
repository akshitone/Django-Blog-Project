from django.http import HttpResponse
from django.shortcuts import render

# def home_page(request):
#     return HttpResponse("Hello world")

def home_page(request):
    title_here = "Akshit Mithaiwala"
    return render(request, "index.html", {"title": title_here})

def aboutus_page(request):
    return render(request, "aboutus.html")