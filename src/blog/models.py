from django.db import models


# Create your models here.
class BlogPost(models.Model):
#   id    = models.IntegerField() -> Primary key
    title   = models.CharField(max_length=120)
    slug    = models.SlugField(unique=True) # hello world = hello-world in this url we want.
    content = models.TextField(null=True, blank=True)

