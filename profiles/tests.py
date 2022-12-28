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
    View.
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_root_route(self):
        """
        Tests whether a logged in user can access the
        Root Route view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_profile_list_view(self):
        """
        Tests whether a logged in user can access the
        Profiles List view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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
        second_username = 'PatThePostMan'
        second_password = 'GoodbyeMoon1234'
        self.second_user = get_user_model().objects.create_user(
            username=second_username,
            password=second_password
        )

    def test_non_logged_in_profile_detail_view(self):
        """
        Test whether a non-logged in user can view a Profile
        Detail View. Should return a HTTP 200 response.
        """
        response = self.client.get('/profiles/1')
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_logged_in_profile_detail_view(self):
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get(f'/profiles/{self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_can_edit_profile(self):
        """
        Test whether a logged in user can edit their profile.
        Tests by attempt to edit name. Should return a
        HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        view = self.client.get(f'/profiles/{self.user.id}')
        self.assertEqual(view.status_code, status.HTTP_200_OK)
        self.assertEqual(view.data['name'], '')
        response = self.client.put(
            f'/profiles/{self.user.id}',
            {'name': 'Changename'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Changename")

    def test_non_logged_in_user_cant_edit_profile(self):
        """
        Tests whether a non-logged in user can edit a user's Profile.
        Tests by attempt to edit name field. Should return a HTTP 400 Bad
        Request response.
        """
        response = self.client.put(
            f'/profiles/{self.user.id}',
            {'name': 'Changename'}
        )
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_other_user_cant_edit_profile(self):
        """
        Tests whether a user that is logged in can edit another user's Profile.
        Test by attempt to edit name field. Should return a HTTP 400 Bad
        Request response.
        """
        self.client.login(username='PatThePostMan',
                          password='GoodbyeMoon1234')
        response = self.client.put(
            f'/profiles/{self.user.id}',
            {'name': 'Changename'}
        )
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
