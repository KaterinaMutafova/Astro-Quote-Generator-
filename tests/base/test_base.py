from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class QuotesTestCase(TestCase):
    logged_in_user_email = 'kat2'
    logged_in_user_password = '12342dodo'

    def assertListEmpty(self, ll):
        return self.assertEqual([], ll, 'The list is not empty.')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        self.user.save()