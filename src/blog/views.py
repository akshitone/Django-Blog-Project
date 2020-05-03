from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def blog_page(request):
    obj = BlogPost.objects.get(id=1)
    return render(request, "blog.html", {"object": obj})
