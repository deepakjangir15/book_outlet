from django.contrib import admin


from .models import Book
# Register your models here.


## Use this BookAdmin class to set various setting, to overwrite various properties in this class
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author','rating')
    list_display = ('title','author')


admin.site.register(Book, BookAdmin)