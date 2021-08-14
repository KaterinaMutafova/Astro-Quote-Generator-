from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse

from quote_generator.profiles.models import UserProfile
from tests.base.test_base import QuotesTestCase


# class test_profile_model_no_data()


UserModel = get_user_model()

class ProfileDetailsTest(QuotesTestCase):
    def setUp(self) -> None:
        group_name = "Regular user"
        self.my_regular_group = Group(name=group_name)
        self.my_regular_group.save()

        self.client = Client()
        self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = UserProfile.objects.get(pk=self.user.id)
        # self.my_regular_group.user_set.add(self.user)

    def test_profile_exists(self):
        # self.profile = UserProfile.objects.get(pk=self.user.id)
        self.assertIsNotNone(self.profile)

    def test_if_default_colour_theme_is_1(self):
        # self.profile = UserProfile.objects.get(pk=self.user.id)
        self.assertEqual(int(self.profile.theme_profile), 1)


    def test_exist_group(self):
        # self.my_regular_group = Group.objects.get(name="Regular user")
        self.assertIsNotNone(self.my_regular_group)


    def test_user_in_group(self):
        self.assertIsNotNone(self.my_regular_group.user_set)
        is_in_group = self.user.groups.filter(name="Regular user").exists()
        self.assertTrue(is_in_group)


    def test_getDetails_whenLoggedInUser_shouldGetDetails(self):
        self.client.force_login(self.user)
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = UserProfile.objects.get(pk=self.user.id)

        response = self.client.get(reverse('profile_home_page'))

        self.assertTemplateUsed(response, 'profile_home_page.html')

        profile = response.context['profile']
        quotes_added_by_user = response.context['quotes_added_by_user']

        self.assertListEmpty(quotes_added_by_user)
        self.assertEqual(self.user.id, profile.user_id)
