

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # A field to store the book's title
    author = models.CharField(max_length=255)  # A field to store the book's author
    published_date = models.DateField()  # A field to store the book's published date
    isbn_number = models.CharField(max_length=13, unique=True)  # A field for the ISBN number

    def __str__(self):
        return self.title  # This method defines how the object is represented
