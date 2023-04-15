from django.contrib import admin
from .models import Category, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display_links = ("slug",)
    list_display = ( "home", "slug","category")
    list_editable = ("home","category")
    search_fields = ("bookname", "description")
    list_filter = ("category", "home")
admin.site.register(Category)
admin.site.register(Book, BookAdmin)