# creating and testing permissions and test groups in django tests.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.http import request

from quote_generator.auth_quotes.managers import QuoteUserManager
from quote_generator.auth_quotes.models import QuoteUser
from django.test import TestCase
from django.test import Client

from quote_generator.profiles.models import UserProfile
from quote_generator.quotes.forms import AuthorForm, QuoteForm
from quote_generator.quotes.models import Quote, Author
from quote_generator.quotes.models.choices import ZODIAC_CHOICES, ELEMENT_CHOICES

UserModel = get_user_model()


class ExampleGroupPermissionsTests(TestCase):

    def setUp(self) -> None:
        group_name = "Regular user"
        self.my_regular_group = Group(name=group_name)
        self.my_regular_group.save()

        self.client = Client()
        self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
        self.my_regular_group = Group.objects.get(name="Regular user")
        # self.my_special_group = Group.objects.get(name="Special user")
        self.profile = UserProfile.objects.get(pk=self.user.id)
        # self.my_regular_group.user_set.add(self.user)

    def tearDown(self):
        self.user.delete()
        self.my_regular_group.delete()
        # self.my_special_group.delete()


    def test_user_in_regular_group(self):
        self.assertIsNotNone(self.my_regular_group.user_set)
        is_in_group = self.user.groups.filter(name="Regular user").exists()
        self.assertTrue(is_in_group)

    def test_user_in_special_group(self):
        # Create author
        the_author_form = AuthorForm(
            {'name': 'Rumi',
            'profession':'poet',
            'description':'something',
            'image': None}
        )
        self.assertTrue(the_author_form.is_valid())
        self.the_author_object = the_author_form.save()
        self.assertIsNotNone(self.the_author_object)

        # Create quote
        the_author_object = the_author_form.save()


        the_quote_form = QuoteForm( {
            'quote': 'Това, което търсиш, търси теб.',
            'author': the_author_object,
            'sign': ZODIAC_CHOICES[1],
            'element': ELEMENT_CHOICES[1],
            'image': None,
            }
        )
        self.assertTrue(the_quote_form.is_valid())
        # self.the_quote_object = the_quote_form.save(commit=False)
        # self.the_quote_object.added_by = self.user
        # self.the_quote_object.save()
        # self.assertIsNotNone(self.the_quote_object)








    # def test_user_cannot_access(self):
    #     """user NOT in group should not have access
    #     """
    #     self.c.login(email="test1@.com", password="1234test1")
    #     response = self.c.get("/my_view")
    #     self.assertEqual(response.status_code, 302, u'user in group should have access')
    #
    # def test_user_can_access(self):
    #     """user in group should have access
    #     """
    #     self.user.groups.add(self.group)
    #     self.user.save()
    #     self.c.login(username='test', password='test')
    #     response = self.c.get("/my_view")
    #     self.assertEqual(response.status_code, 200, u'user in group should have access')