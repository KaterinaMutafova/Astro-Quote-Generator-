from django.urls import path
from quote_generator.profiles.views import logout_user, login_user, register_user
from quote_generator.quotes import views
from quote_generator.quotes.views import add_quote

urlpatterns = [
    path('', views.base, name='index'),
    path('register_user', register_user, name='register_user'),
    path('login_user', login_user, name='login_user'),
    path('logout_user', logout_user, name='logout_user'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quote_details/<int:pk>', views.quote_details, name='quote_details'),
    path('edit_quote/<int:pk>', views.edit_quote, name='edit_quote'),
    path('delete_quote/<int:pk>', views.delete_quote, name='delete_quote'),
    path('change_quote/', views.change_quote, name='change_quote'),
    path('show_all_quotes/', views.show_all_quotes, name='show_all_quotes'),
    path('show_all_authors', views.show_all_authors, name='show_all_authors'),
    path('add_author/', views.add_author, name='add_author'),
    path('elements_index/', views.elements_index, name='elements_index')

]