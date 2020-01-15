from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_create_with_email_successful(self):
        """test creating new user with email successful"""
        email = 'test@user.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = 'test@UPPERCASEPART.com'
        user = get_user_model().objects.create_user(email, 'Test123')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """test user with no email provided"""
        """assertRaises jest jak try... except czyli tutaj
         testujemy dla okreslonego errora"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@superuser.com',
            'Test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
