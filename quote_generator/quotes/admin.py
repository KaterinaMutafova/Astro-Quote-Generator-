from django.contrib import admin

# Register your models here.
from quote_generator.quotes.models import Author, Quote


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'profession', 'description']
    list_display = ['name', 'profession', 'description']
    list_filter = ['name', 'profession']


class QuoteAdmin(admin.ModelAdmin):
    fields = ['quote', 'author', 'sign', 'element', 'added_by']
    list_display = ['quote', 'author', 'sign', 'element', 'added_by']
    list_filter = ['author', 'sign', 'element', 'added_by']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
