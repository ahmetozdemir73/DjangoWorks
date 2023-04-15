from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("books", views.books, name="books"),
    path("category/<slug:slug>", views.books_by_category, name = "books_by_category"),
    path("books/<id>", views.bookdetails, name="bookdetails"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

