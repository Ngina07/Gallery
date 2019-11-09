from django.test import TestCase
from .models import Location,categories,Image


class categoriesTestClass(TestCase):
    def setUp(self):
        self.Random = categories(category = 'Random')

    def test_instance(self):
        self.assertTrue(isinstance(self.Random,categories))

    def tearDown(self):
        categories.objects.all().delete()

    def test_save_method(self):
        self.Random.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category)>0)
    def test_delete_method(self):
        self.Random.delete_category('Random')
        category = categories.objects.all()
        self.assertTrue(len(category)==0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.Somewhere = Location(location = 'Somewhere')

    def test_instance(self):
        self.assertTrue(isinstance(self.Somewhere,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Somewhere.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Somewhere.delete_location('Somewhere')
        location = Location.objects.all()
        self.assertTrue(len(location)==0)
