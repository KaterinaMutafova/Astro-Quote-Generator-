from django.urls import path
from quote_generator.profiles import views

urlpatterns = [
    path('profile/', views.profile_home_page, name='profile_home_page'),

]

