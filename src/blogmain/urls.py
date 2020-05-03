from django.contrib import admin
from django.urls import path

from blog.views import (
    blog_page
)

from .views import (
    home_page,
    aboutus_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('aboutus/', aboutus_page),
    path('contact/', home_page),
    path('blog/', blog_page)
]
