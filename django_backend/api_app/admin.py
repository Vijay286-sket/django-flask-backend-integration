from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn_number')  # Columns shown in the admin list
    search_fields = ('title', 'author')  # Search bar for title and author

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)


