from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client

from quote_generator.profiles.models import UserProfile

UserModel = get_user_model()


class LoginTest(TestCase):
    def setUp(self) -> None:
        group_name = "Regular user"
        self.my_regular_group = Group(name=group_name)
        self.my_regular_group.save()

        self.client = Client()
        self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = UserProfile.objects.get(pk=self.user.id)

    def test_login(self):
        login = self.client.login(email='kat1@abv.bg', password='12341dodo')
        self.assertTrue(login)

    def test_unsuccessfull_login(self):
        login = self.client.login(email='test@abv.bg', password='1234')
        self.assertFalse(login)