from django.test import TestCase, Client
from main.models import Vehicle
import random as r

# Create your tests here.
class mainTest(TestCase):
    def setUp(self):
        Vehicle.objects.create(name="Manusia", amount=7888000000, description="ketabrak", image_link="")
        Vehicle.objects.create(name='Becak',amount=20, description='bekekekek',image_link="")

    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_becak_exist(self):
        becak = Vehicle.objects.get(name="Becak")
        self.assertEqual(becak.name, "Becak")
        self.assertEqual(becak.description, 'bekekekek')
        self.assertEqual(becak.image_link, "")
        self.assertEqual(becak.amount, 20)
    
    def test_manusia_exist(self):
        manusia = Vehicle.objects.get(name="Manusia")
        self.assertEqual(manusia.name, "Manusia")
        self.assertEqual(manusia.description, 'ketabrak')
        self.assertEqual(manusia.image_link, "")
        self.assertEqual(manusia.amount, 7888000000)
