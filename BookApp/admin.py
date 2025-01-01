from django.contrib import admin
from .models import BookModel
# Register your models here.
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
admin.site.register(BookModel, BookModelAdmin)
