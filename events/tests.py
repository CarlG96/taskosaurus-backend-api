"""
File for testing Taskosaurus Event Model
"""
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from profiles import models
from events import models


class TestEventListView(APITestCase):
    """
    Class to perform automated tests on the
     Event List View.
    """
    def setUp(self):
        """
        Standard APITestCase setUp function. Creates a user
        for the test database. Also creates some Tasks.
        """
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        event = models.Event.objects.create(title="Hello World",
                                            date_of_event="2023-08-15 15:20",
                                            need_travel=True,
                                            money_required=10,
                                            owner=self.user)
    
    def test_logged_out_event_list_view(self):
        """
        Tests whether a non-logged in user can access the Event List
        view. Should return a HTTP 200 Response.
        """
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_event_list_view(self):
        """
        Tests whether a logged in user can access the Event List
        view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_post_event(self):
        """
        Tests whether a logged in user can create an Event in the
        Event List View. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "Hello World",
                "date_of_event": "2023-08-15 15:20",
                "owner": f"{self.user}",
                "money_required": 10,
                "need_travel": True}
        response = self.client.post('/events/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Hello World")
        self.assertEqual(response.data["date_of_event"], "15:20 15 Aug 2023")
        self.assertEqual(response.data["money_required"], 10)
        self.assertEqual(response.data["need_travel"], True)
        self.assertEqual(response.data["owner"], f"{self.user}")

    def test_logged_out_user_cant_post_event(self):
        """
        Tests whether a logged out user can create an Event in the
        Event List View. Should return a HTTP 403 response.
        """
        data = {"title": "Hello World",
                "date_of_event": "2023-08-15 15:20",
                "owner": f"{self.user}",
                "money_required": 10,
                "need_travel": True}
        response = self.client.post(f'/events/', data)
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_event_must_have_valid_date_of_event(self):
        """
        Tests whether the validation for the date of event
        for the Event is working correctly. Should return
        a HTTP 400 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "Hello World",
                "date_of_event": "2021-08-15 15:20",
                "owner": f"{self.user}",
                "money_required": 10,
                "need_travel": True}
        response = self.client.post(f'/events/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_event_must_have_valid_title(self):
        """
        Tests whether the validation for the title for the
        Event is working correctly. Should return a HTTP 400
        response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "",
                "date_of_event": "2023-08-15 15:20",
                "owner": f"{self.user}",
                "money_required": 10,
                "need_travel": True}
        response = self.client.post(f'/events/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

class EventDetailView(APITestCase):
    """
    Class to perform tests on the Event Detail View.
    """
    def setUp(self):
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        event = models.Event.objects.create(title="Hello World",
                                            date_of_event="2023-08-15 15:20",
                                            need_travel=True,
                                            money_required=10,
                                            owner=self.user)