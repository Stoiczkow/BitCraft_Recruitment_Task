from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from .models import Links
# Create your tests here.


class TestCreateLink(TestCase):
    def setUp(self):
        self.client = Client()
        self.client_not_logged = Client()
        self.user = User.objects.create()
        self.client.force_login(user=self.user)

    def test_response_logged(self):
        response = self.client.get('/add_link/')
        self.assertEqual(response.status_code, 200)

    def test_response_not_logged(self):
        response = self.client_not_logged.get('/add_link/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_form(self):
        response = self.client.get('/add_link/')
        data = response.content.decode('utf-8')
        self.assertIn('<form', data)

    def test_post_valid(self):
        response = self.client.post('/add_link/',
                                    {'address': 'www.google.com'}, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_redirection(self):
        link = Links.objects.create(address='www.google.com')
        link.save()
        response = self.client.get('/get_link/{}/'.format(link.token),
                                   follow=True)

        self.assertEqual(response.status_code, 200)


class TestCreateFile(TestCase):
    def setUp(self):
        self.client = Client()
        self.client_not_logged = Client()
        self.user = User.objects.create()
        self.client.force_login(user=self.user)

    def test_response_logged(self):
        response = self.client.get('/add_file/')
        self.assertEqual(response.status_code, 200)

    def test_response_not_logged(self):
        response = self.client_not_logged.get('/add_file/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_form(self):
        response = self.client.get('/add_file/')
        data = response.content.decode('utf-8')
        self.assertIn('<form', data)

    def test_post_valid(self):
        response = self.client.post('/add_file/',
                                    {'file': 'example.txt'}, follow=True)

        self.assertEqual(response.status_code, 200)
