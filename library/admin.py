from django.contrib import admin
from .models import Author, Category, Book, Loan, CustomUser

# Registering the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography')
    search_fields = ('name',)

admin.site.register(Author, AuthorAdmin)

# Registering the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

# Registering the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'isbn', 'published_date', 'copies_available')
    list_filter = ('author', 'category', 'published_date')
    search_fields = ('title', 'isbn')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

admin.site.register(Book, BookAdmin)

# Registering the Loan model
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'loaned_to', 'loaned_date', 'return_date')
    list_filter = ('loaned_date', 'return_date', 'book')
    search_fields = ('loaned_to',)

admin.site.register(Loan, LoanAdmin)

# Registering the CustomUser model
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
