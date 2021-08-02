from django.urls import path
from quote_generator.profiles import views

urlpatterns = [
    path('profile/', views.profile_home_page, name='profile_home_page'),
    path('edit_profile/<int:pk>', views.edit_profile, name='edit_profile'),

]

