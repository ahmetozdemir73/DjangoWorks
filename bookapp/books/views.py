from django.shortcuts import render
from .models import Category, Book

"""
category_list = ["Polisiye", "Tarih", "Macera", "Bilim Kurgu"]
book_list =[
    {
        "id":1,
        "bookname": "Kitap1",
        "author": "author1",
        "description": "kitap1 açıklama",
        "image": "1.jpeg",
        "home": True
    },
    {
        "id":2,
        "bookname": "Kitap2",
        "author": "author2",
        "description": "kitap2 açıklama",
        "image": "2.jpeg",
        "home": True
    },
    {
        "id":3,
        "bookname": "Kitap3",
        "author": "author3",
        "description": "kitap3 açıklama",
        "image": "3.jpeg",
        "home": True
    },
    {
        "id":4,
        "bookname": "Kitap4",
        "author": "author4",
        "description": "kitap4 açıklama",
        "image": "4.jpeg",
        "home": False
    },
    ]
"""
# Create your views here.
def home(request):
    data = {
        "categories": Category.objects.all,
        "books": Book.objects.filter(home=True)
    }
    return render(request, "index.html", data)

def books(request):
    data = {
        "categories": Category.objects.all,
        "books": Book.objects.all
    }
    return render(request, "books.html",data)

def bookdetails(request, id):
    data = {
        "book": Book.objects.get(id = id)
    }
    return render(request, "details.html",data)

def books_by_category(request, slug):
    data = {
        "categories": Category.objects.all,
        "books": Book.objects.filter(category__slug=slug),
        "selected_category":slug,
    }
    return render(request, "books.html",data)