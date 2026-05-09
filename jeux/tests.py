from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Jeu

class JeuModelTest(TestCase):
    def setUp(self):
        self.jeu = Jeu.objects.create(
            name="Test Game",
            description="A test game description",
            release_date="2024-01-01",
            genre="Action",
            developer="Test Dev",
            publisher="Test Pub"
        )

    def test_jeu_creation(self):
        self.assertEqual(self.jeu.name, "Test Game")
        self.assertEqual(str(self.jeu), "Test Game")

class JeuAPITest(APITestCase):
    def setUp(self):
        self.jeu = Jeu.objects.create(
            name="API Game",
            description="API test description",
            release_date="2024-01-01",
            genre="RPG",
            developer="API Dev",
            publisher="API Pub"
        )

    def test_get_jeu_list(self):
        url = '/jeux/api/jeu-api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

class JeuViewTest(TestCase):
    def test_jeu_list_view(self):
        url = reverse('jeu_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jeux/jeu_list.html')
