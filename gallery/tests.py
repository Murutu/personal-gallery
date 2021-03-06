from django.test import TestCase
from .models import Image,Category,tags

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.Image= Image(image_title= 'cars', image_description ='great cars')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cars,Image))
        
    # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)    
