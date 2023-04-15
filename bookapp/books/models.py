from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, blank=True,unique=True,db_index=True,editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    bookname = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to="books")
    home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True,unique=True,db_index=True,editable=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.bookname)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.bookname