from django.urls import path

from .views import (
    blogpost_list,
    blog_page
)


urlpatterns = [
    path('', blogpost_list),
    path('<str:slug>', blog_page)
]
