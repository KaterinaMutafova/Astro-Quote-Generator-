from django import template

from quote_generator.profiles.models import UserProfile

register = template.Library()


@register.simple_tag(name="get_color_theme")
def get_color_theme(request):
    if request.user.is_anonymous:
        color_theme_index = 0
    else:
        profile = UserProfile.objects.get(pk=request.user.id)
        color_theme_index = profile.theme_profile
    return int(color_theme_index)



# color_theme_index = ''
#     if request.user.is_anonymous:
#         color_theme_index = 0
#     elif request.user.is_superuser:
#         color_theme_index = 1
#     else:
#         color_theme_index = 4
#     return color_theme_index