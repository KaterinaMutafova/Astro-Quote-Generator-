from django.contrib import admin

# Register your models here.
from quote_generator.quotes.models import Author, Quote


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'profession']
    list_display = ['name', 'profession']
    list_filter = ['name']


class QuoteAdmin(admin.ModelAdmin):
    fields = ['quote', 'author', 'sign', 'element']
    list_display = ['quote', 'author', 'sign', 'element']
    list_filter = ['author', 'sign', 'element']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
