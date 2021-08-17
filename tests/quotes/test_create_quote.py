from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.test import TestCase
from django.test import Client

from quote_generator.profiles.models import UserProfile
from quote_generator.quotes.forms import AuthorForm, QuoteForm
from quote_generator.quotes.models import Quote

UserModel = get_user_model()

class TestCreateQuote(TestCase):

    def setUp(self) -> None:
        # Create Regular user group
        regular_group_name = "Regular user"
        self.my_regular_group = Group(name=regular_group_name)
        self.my_regular_group.save()
        self.my_regular_group = Group.objects.get(name="Regular user")

        # Create Special user group
        special_group_name = "Special user"
        self.my_special_group = Group(name=special_group_name)
        self.my_special_group.save()
        self.my_special_group = Group.objects.get(name="Special user")

        # Create user and profile
        self.client = Client()
        self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
        self.profile = UserProfile.objects.get(pk=self.user.id)
        self.my_regular_group.user_set.add(self.user)

        # Create author:
        self.the_author_form = AuthorForm(
            {'name': 'Rumi',
             'profession': 'poet',
             'description': 'something',
             'image': None}
        )
        self.the_author_object = self.the_author_form.save()
        self.the_author_object.full_clean()
        self.the_author_object.save()


    def test_create_quote_model(self):
        # Create quote model
        the_quote_form = QuoteForm(
            {'quote': 'Това, което търсиш, търси теб.',
             'author': self.the_author_object,
             'sign':'стрелец',
             'element': 'огън',
             'image': None,
             'added_by': self.user,
             }
        )

        self.assertTrue(the_quote_form.is_valid())

        the_quote_object = the_quote_form.save()
        the_quote_object.full_clean()
        the_quote_object.save()

        self.assertIsNotNone(the_quote_object)

    def test_create_three_quotes_add_to_special_user_group(self):
        # Create quote model
        the_quote_form = QuoteForm(
            {'quote': 'Това, което търсиш, търси теб.',
             'author': self.the_author_object,
             'sign':'стрелец',
             'element': 'огън',
             'image': None,
             'added_by': self.user,
             }
        )

        self.assertTrue(the_quote_form.is_valid())

        the_quote_object = the_quote_form.save()
        the_quote_object.full_clean()
        the_quote_object.save()

        self.assertIsNotNone(the_quote_object)

        # Create quote model 2
        the_quote_form = QuoteForm(
            {'quote': 'Това, което търсиш, търси теб.',
             'author': self.the_author_object,
             'sign': 'стрелец',
             'element': 'огън',
             'image': None,
             'added_by': self.user,
             }
        )

        self.assertTrue(the_quote_form.is_valid())

        the_quote_object2 = the_quote_form.save()
        the_quote_object2.full_clean()
        the_quote_object2.save()

        self.assertIsNotNone(the_quote_object2)

        # Create quote model 3
        the_quote_form = QuoteForm(
            {'quote': 'Това, което търсиш, търси теб.',
             'author': self.the_author_object,
             'sign': 'стрелец',
             'element': 'огън',
             'image': None,
             'added_by': self.user,
             }
        )

        self.assertTrue(the_quote_form.is_valid())

        the_quote_object3 = the_quote_form.save()
        the_quote_object3.full_clean()
        the_quote_object3.save()

        self.assertIsNotNone(the_quote_object3)

        self.assertEqual(the_quote_object3.added_by, self.user)

        all_quotes = Quote.objects.all()
        self.assertEqual(len(all_quotes), 3)

        self.assertIsNotNone(self.my_special_group.user_set)
        is_in_group = self.user.groups.filter(name="Special user").exists()
        self.assertTrue(is_in_group)


