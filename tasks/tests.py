"""
File for testing Taskosaurus Note Model
"""
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from profiles import models
from tasks import models


class TestTaskListView(APITestCase):
    """
    Class to perform automated tests on the
    Task List View.
    """
    def setUp(self):
        """
        Standard APITestCase setUp function. Creates a user
        for the test database. Also creates some Tasks
        """
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        task = models.Task.objects.create(title="Hello World",
                                          due_date="2023-08-15 15:20",
                                          state="Archived",
                                          priority="Might Do",
                                          owner=self.user)

    def test_logged_out_task_list_view(self):
        """
        Tests whether a non-logged in user can access the Task List
        view. Should return a HTTP 200 Response.
        """
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_task_list_view(self):
        """
        Tests whether a logged in user can access the Task List
        view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_post_task(self):
        """
        Tests whether a logged in user can create a Task in the
        Task List View. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "Hello World",
                "due_date": "2023-08-15 15:20",
                "owner": f"{self.user}"}
        response = self.client.post('/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Hello World")
        self.assertEqual(response.data["due_date"], "15:20 15 Aug 2023")
        self.assertEqual(response.data["owner"], f"{self.user}")

    def test_logged_out_user_cant_post_task(self):
        """
        Tests whether a logged out user can create a Task in the
        Task List View. Should return a HTTP 403 response.
        """
        data = {"title": "Hello World",
                "due_date": "2023-02-15 15:20",
                "owner": f"{self.user}"}
        response = self.client.post(f'/tasks/', data)
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_post_must_have_valid_due_date(self):
        """
        Tests whether the validation for the due date for the Task
        is working correctly. Should return a HTTP 400 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "Hello World",
                "due_date": "2021-02-15 15:20",
                "owner": f"{self.user}"}
        response = self.client.post(f'/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_must_have_valid_title(self):
        """
        Tests whether the validation for the title for the Task
        is working correctly. Should return a HTTP 400 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "",
                "due_date": "2023-02-15 15:20",
                "owner": f"{self.user}"}
        response = self.client.post(f'/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestTaskDetailView(APITestCase):
    """
    Class to perform automated tests on the
    Task Detail View.
    """
    def setUp(self):
        username = 'BobTheBuilder'
        password = 'HelloWorld1234'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        task = models.Task.objects.create(title="Hello World",
                                          due_date="2023-02-15 15:20",
                                          state="Archived",
                                          priority="Might Do",
                                          owner=self.user)

    def test_logged_out_task_detail_view(self):
        """
        Tests whether a non-logged in user can access the
        Task Detail view. Should return a HTTP 404 response.
        """
        response = self.client.get('/tasks/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_task_detail_view(self):
        """
        Tests whether a logged in user can access the
        Task Detail view of a Task they own. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.get('/tasks/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_other_user_detail_view(self):
        """
        Tests whether a logged in user can access the
        Task Detail view of a Task they don't own. Should return a HTTP 404 
        response.
        """
        second_username = 'PatThePostMan'
        second_password = 'GoodbyeMoon1234'
        self.second_user = get_user_model().objects.create_user(
            username=second_username,
            password=second_password
        )
        self.client.login(username=second_username,
                          password=second_password)
        response = self.client.get('/tasks/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_can_update_task(self):
        """
        Tests whether an owner can change a Task in
        the Task Detail view. Should return a HTTP 200 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        response = self.client.put('/tasks/1',
                                   {'title': 'change'})
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_whether_non_owner_cant_update_task(self):
        """
        Tests whether a non-owner can change a Task in
        the Task Detail view. Should return a
        HTTP 403 response.
        """
        second_username = 'PatThePostMan'
        second_password = 'GoodbyeMoon1234'
        self.second_user = get_user_model().objects.create_user(
            username=second_username,
            password=second_password
        )
        self.client.login(username=second_username,
                          password=second_password)
        response = self.client.put('/tasks/1',
                                   {'title': 'change'})
        self.assertTrue(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_must_have_valid_due_date(self):
        """
        Tests whether an owner's put request must have a
        valid due date field. Should return a HTTP
        400 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "Hello World",
                "due_date": "2021-02-15 15:20",
                "owner": f"{self.user}"}
        response = self.client.put(f'/tasks/1', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_must_have_valid_title(self):
        """
        Tests whether an owner's put request must have a
        valid title field. Should return a HTTP
        400 response.
        """
        self.client.login(username='BobTheBuilder',
                          password='HelloWorld1234')
        data = {"title": "",
                "due_date": "2023-02-15 15:20",
                "owner": f"{self.user}"}
        response = self.client.put(f'/tasks/1', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)