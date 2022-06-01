from turtle import title
from django.test import TestCase
from .models import Images,Categorys,Locations

# Create your tests here.
class ImagesTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.giyuu_Tomioka= Images(img_name=" giyuu_Tomioka",description="ara",image="assets/css/images")
    def test_instance(self):
        self.assertTrue(isinstance(self.giyuu_Tomioka,Images))
    # Testing Save Method
    def test_save_method(self):
        self.giyuu_Tomioka.save_images()
        images= Images.objects.all()
        self.assertTrue(len(images) > 0)

class LocationsTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.tokyo= Locations(location_name = "Tokyo")
    def test_instance(self):
        self.assertTrue(isinstance(self.tokyo,Locations))
    # Testing Save Method
    def test_save_method(self):
        self.tokyo.save_Locations()
        locations= Locations.objects.all()
        self.assertTrue(len(locations) > 0)

class CategorysTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.food= Categorys(image_category ="Action")

    def test_instance(self):
        self.assertTrue(isinstance(self.action,Categorys))

    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        categories= Categorys.objects.all()
        self.assertTrue(len(categories) > 0)

    def tearDown(self):
        Locations.objects.all().delete()
        Categorys.objects.all().delete()
        Images.objects.all().delete()