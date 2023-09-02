from django.test import TestCase
from .models import faq
from django.contrib.auth import get_user_model

# Create your tests here.

class TestViews(TestCase):
    """
    Test cases for faq app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = "Rupa"
        password = "rupa@studyalong"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True,
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_ans_faq(self):
        """ Test course detail """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class TestUnsecuredViews(TestCase):
    """ Test views no auth required """
    def test_post_faq(self):
        """ Test view menu """
        response = self.client.get('/faq/post-faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_faq.html')
    
    def test_view_faq(self):
        """ Test course detail """
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')
    def test_ans_faq(self):
        """ Test course detail """
        response = self.client.get('/faq/ans-faq/5')
        self.assertEqual(response.status_code, 301)
    