from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Bookcourse

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

    def test_view_booking(self):
        """ Test booking detail """
        response = self.client.get('/mybooking/view-booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_detail.html')

    def test_search_booking(self):
        """ Test booking detail """
        response = self.client.get('/mybooking/search-booking/?q=Kabyik Pal')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_booking.html')

    def test_delete_booking(self):
        """ Test booking detail """
        response = self.client.get('/mybooking/delete/7/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_confirm_delete.html')

    def test_edit_booking(self):
        """ Test booking detail """
        response = self.client.get('/mybooking/edit/10/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')



class TestUnsecuredViews(TestCase):
    """ Test views no auth required """
    
    def test_view_booking(self):
        """ Test booking detail """
        response = self.client.get('/mybooking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')
        