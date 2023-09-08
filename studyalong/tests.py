from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course

# Create your tests here.


class TestViews(TestCase):
    """
    Test cases for menu app as logged in user
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

    def test_create_menu_page(self):
        """ Test course detail """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_create_course(self):
        """ Test redirect on create course """
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)

    def test_check_course(self):
        """ Test redirect on create course """
        response = self.client.get('/check-course/3?course=Street Dance')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'check_course.html')

    def test_course_detail(self):
        """ Test redirect on course detail """
        response = self.client.get('/details/3')
        self.assertEqual(response.status_code, 200)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """

    def test_edit_course(self):
        """ Test redirect on create course """
        response = self.client.get('/edit/1')
        self.assertEqual(response.status_code, 302)
