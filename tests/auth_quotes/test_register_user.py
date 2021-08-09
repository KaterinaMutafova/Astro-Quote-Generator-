from django.test import TestCase, Client

from quote_generator.auth_quotes.forms import RegisterForm



class RegisterUser(TestCase):
    # def setUp(self) -> None:
    #     # self.client = Client()
    #     self.email = 'kat4@abv.bg'
    #     self.password1 = '12344dodo'
    #     self.password2 = '12344dodo'

    def test_check_with_valid_data_if_form_is_valid(self):
        user_form = RegisterForm(
            {'email': 'kat4@abv.bg',
            'password1': '12344dodo',
            'password2': '12344dodo',}
        )
        self.assertTrue(user_form.is_valid())

    def test_check_with_invalid_date_if_form_is_valid(self):
        user_form = RegisterForm(
            {'email': 'kat4@abv.bg',
             'password1': '12344dodo',
             'password2': '12344dod', }
        )
        self.assertFalse(user_form.is_valid(), msg='Двете пароли не  съвпадат.')

    def test_check_form_with_invalid_email(self):
        user_form = RegisterForm(
            {'email': 'kat4',
             'password1': '12344dodo',
             'password2': '12344dodo', }
        )
        self.assertFalse(user_form.is_valid(), msg='Enter a valid email address.')


    def test_check_form_with_too_short_password(self):
        user_form = RegisterForm(
            {'email': 'kat4@abv.bg',
             'password1': '12dodo',
             'password2': '12dodo', }
        )
        self.assertFalse(user_form.is_valid(), msg='This password is too short. It must contain at least 8 characters.')


    def test_check_form_with_numeric_password(self):
        user_form = RegisterForm(
            {'email': 'kat4@abv.bg',
             'password1': '12345678',
             'password2': '12345678', }
        )
        self.assertFalse(user_form.is_valid(), msg='This password is entirely numeric.')











