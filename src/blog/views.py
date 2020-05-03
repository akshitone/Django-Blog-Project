from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import BlogPost
#  from django.http import HttpResponse

# Create your views here.

def blog_page(request, slug):
     # try:
     #     obj = BlogPost.objects.get(id=post_id)  #Query -> Database -> Data -> Django render
     # except:
     #     #  return HttpResponse("Hello world")
     #     raise Http404


     ##obj = get_object_or_404(BlogPost, slug=slug)

     #get -> 1 object
     #fliter -> [] object
     # queryset = BlogPost.objects.filter(slug=slug)
     # if queryset.count() == 0:
     #     raise Http404
     # obj = queryset.first()
     try:
         obj = BlogPost.objects.get(slug=slug)
     except:
         raise Http404

     template_name = "blog.html"
     context = {"object": obj}
     return render(request, template_name, context)

#CRUD
#GET -> RETRIVE / LIST
#POST -> CREATE / UPDATE / DELETE

def blogpost_list(request):
    #listout object
    #could be search
    query = BlogPost.objects.all()
    template_name = "BlogList.html"
    context = {"object_list": query}
    return render(request, template_name, context)

def blogpost_add(request):
    template_name = "BlogAdd.html"
    context = {"form": None}
    return render(request, template_name, context)

def blogpost_view(request, slug):
    #1 object -> detailed view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "BlogView.html"
    context = {"object": obj}
    return render(request, template_name, context)

def blogpost_update(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "BlogView.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)

def blogpost_delete(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "BlogView.html"
    context = {"object": obj}
    return render(request, template_name, context)
