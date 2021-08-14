from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from quote_generator.auth_quotes.forms import RegisterForm
from quote_generator.auth_quotes.managers import QuoteUserManager
from quote_generator.auth_quotes.models import QuoteUser
from quote_generator.profiles.models import UserProfile

UserModel = get_user_model()

class RegisterUser(TestCase):
    # def setUp(self) -> None:
    #     group_name = "Regular user"
    #     self.my_regular_group = Group(name=group_name)
    #     self.my_regular_group.save()
    #
    #     self.client = Client()
    #     self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
    #     self.my_regular_group = Group.objects.get(name="Regular user")
    #     self.profile = UserProfile.objects.get(pk=self.user.id)


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



class CreateUser(TestCase):
    def setUp(self) -> None:
        group_name = "Regular user"
        self.my_regular_group = Group(name=group_name)
        self.my_regular_group.save()

        self.client = Client()
        self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
        self.my_regular_group = Group.objects.get(name="Regular user")
        # self.profile = UserProfile.objects.get(pk=self.user.id)

    def test_create_user_instance(self):
        # quote_user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')

        self.assertEquals(False, self.user.is_staff)
        self.assertEquals('kat1@abv.bg', self.user.email)

    def test_create_super_user(self):
        quote_user = UserModel.objects.create_superuser(email='kat2@abv.bg', password='12342dodo')

        self.assertEqual(True, quote_user.is_staff)
        self.assertEquals('kat2@abv.bg', quote_user.email)





