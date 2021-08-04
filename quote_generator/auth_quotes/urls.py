from django.urls import path

from quote_generator.auth_quotes.views import register_user, login_user, logout_user

urlpatterns = [
    path('register_user', register_user, name='register_user'),
    path('login_user', login_user, name='login_user'),
    path('logout_user', logout_user, name='logout_user'),

]

