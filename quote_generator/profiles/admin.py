from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from quote_generator.profiles.models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    fields = ['date_of_birth', 'first_name', 'last_name', 'theme_profile', 'user']
    list_display = ['date_of_birth', 'first_name', 'last_name', 'theme_profile', 'user']
    search_fields = ['first_name', 'last_name', 'date_of_birth']
    list_filter = ('date_of_birth', 'theme_profile', 'user')


admin.site.register(UserProfile, ProfileAdmin)
