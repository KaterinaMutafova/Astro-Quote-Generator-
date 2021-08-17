from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.test import TestCase
from django.test import Client

from quote_generator.profiles.models import UserProfile
from quote_generator.quotes.forms import AuthorForm

UserModel = get_user_model()

class TestCreateAuthor(TestCase):

    def setUp(self) -> None:
        regular_group_name = "Regular user"
        self.my_regular_group = Group(name=regular_group_name)
        self.my_regular_group.save()

        self.client = Client()
        self.user = UserModel.objects.create_user(email='kat1@abv.bg', password='12341dodo')
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = UserProfile.objects.get(pk=self.user.id)
        # self.my_regular_group.user_set.add(self.user)


    def test_create_author_model(self):
        # Create author
        the_author_form = AuthorForm(
            {'name': 'Rumi',
            'profession':'poet',
            'description':'something',
            'image': None}
        )
        self.assertTrue(the_author_form.is_valid())

        the_author_object = the_author_form.save()
        the_author_object.full_clean()
        the_author_object.save()

        self.assertIsNotNone(the_author_object)
