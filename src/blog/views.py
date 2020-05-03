from django.shortcuts import render, get_object_or_404
from django.http import Http404
#  from django.http import HttpResponse

# Create your views here.
from .models import BlogPost

def blog_page(request, post_id):
    # try:
    #     obj = BlogPost.objects.get(id=post_id)  #Query -> Database -> Data -> Django render
    # except:
    #     #  return HttpResponse("Hello world")
    #     raise Http404
    obj = get_object_or_404(BlogPost, id=post_id)
    return render(request, "blog.html", {"object": obj})
