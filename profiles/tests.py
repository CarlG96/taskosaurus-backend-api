"""
File for testing Taskosaurus Profile Model
"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from profiles import models


class TestRootRouteView(APITestCase):
    """
    Class to perform automated tests on the Root Route
    View
    """
    def setUp(self):
        """
        Standard APITestCase setUp function. Creates a user
        for the test database.
        """
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

    def test_logged_out_root_route(self):
        """
        Tests whether a non-logged in user can access the
        Root Route view. Should return a HTTP 200 response.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_root_route(self):
        """
        Tests whether a logged in user can access the
        Root Route view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestProfileListView(APITestCase):
    """
    Class to perform automated testing on the
    Profile List View.
    """

    def setUp(self):
        """
        Standard APITestCase setUp function. Creates a user
        for the test database.
        """
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

    def test_non_logged_in_profile_list_view(self):
        """
        Tests whether a non-logged in user can access the
        Profiles List view. Should return a HTTP 200 response.
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_profile_list_view(self):
        """
        Tests whether a logged in user can access the
        Profiles List view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

   
class TestProfileDetailView(APITestCase):
    """
    Class to perform automated testing on the
    Profile Detail View.
    """
    def setUp(self):
        """
        Standard APITestCase setUp function. Creates a user
        for the test database.
        """
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
    
    def test_non_logged_in_profile_detail_view(self):
        

    

        


