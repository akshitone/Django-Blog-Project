from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
# def home_page(request):
#     return HttpResponse("Hello world")

def home_page(request):
    title_here = "Akshit Mithaiwala"
    return render(request, "index.html", {"title": title_here})

def aboutus_page(request):
    context = {"my_list": []}
    if request.user.is_authenticated:
        context = {"my_list": [1, 2, 3, 4, 5]}
    return render(request, "aboutus.html",context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "form.html", {"title": "Contact Us"})