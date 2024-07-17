from django.test import TestCase
from django.urls import reverse


class CVViewsTestCase(TestCase):
    def test_get_personal(self):
        response = self.client.get(reverse('personal'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json())

    def test_get_experience(self):
        response = self.client.get(reverse('experience'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_get_education(self):
        response = self.client.get(reverse('education'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))
