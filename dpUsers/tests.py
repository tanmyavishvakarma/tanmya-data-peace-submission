from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="James", last_name="Butt", company_name="Benton, John B Jr",
            city="New Orleans", state="LA", zip=70116, email="jbutt@gmail.com",
            web="http://www.bentonjohnbjr.com", age=70
        )

    def test_user_creation(self):
        user = User.objects.get(first_name="James")
        self.assertEqual(user.last_name, "Butt")

class UserAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Josephine", last_name="Darakjy", company_name="Chanay, Jeffrey A Esq",
            city="Brighton", state="MI", zip=48116, email="josephine_darakjy@darakjy.org",
            web="http://www.chanayjeffreyaesq.com", age=48
        )

    def test_get_user_list(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Josephine")

    def test_create_user(self):
        data = {
            "first_name": "Test",
            "last_name": "User",
            "company_name": "Test Company",
            "city": "Test City",
            "state": "TS",
            "zip": 12345,
            "email": "testuser@test.com",
            "web": "http://www.test.com",
            "age": 30
        }
        response = self.client.post('/api/users', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email="testuser@test.com").exists())
