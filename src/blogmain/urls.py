from django.contrib import admin
from django.urls import path, include

from blog.views import (
    blogpost_add,
#     blog_page,
#     blogpost_list,
#     blogpost_update,
#     blogpost_delete,
#     blogpost_view
)

from .views import (
    home_page,
    aboutus_page,
    contact_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('aboutus/', aboutus_page),
    path('contact/', contact_page),
    path('blog/', include('blog.urls')),
    path('blog-add/', blogpost_add)
    # path('blog/', blogpost_list),
    # path('blog-update/', blogpost_update),
    # path('blog-delete/', blogpost_delete),
    # path('blog-view/', blogpost_view)
]
