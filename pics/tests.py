from django.test import TestCase
from .models import Image,location,Category

class ImageTestClass(TestCase):

    def setUp(self):
        self.flower = Image(image_name = 'flower',image_desc ='lovely')

    def test_instance(self):
        self.assertTrue(isinstance(self.flower,Image))

    def test_save_method(self):
        self.flower.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        