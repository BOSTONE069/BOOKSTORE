from django.urls import path
from .views import BookListApi, BookCreateApi, BookUpdateApi, BookDeleteApi



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list', BookListApi),
    path('create', BookCreateApi),
    path('update/<int:id>', BookUpdateApi),
    path('delete/<int:id>', BookDeleteApi),
]