from django.db import models
import pyperclip

# Create your models here.
class Image(models.Model):
    image_title = models.CharField(max_length=60)
    image_description = models.TextField(max_length=500)
    image_category = models.CharField(max_length=30,blank=True)
    image_location = models.CharField(max_length=50,blank=True)
    
    
    
    def __str__(self):
        return self.image_title
    
    def save_image(self):
        self.save()
        
    class Meta:
        ordering = ['image_title']
        
    def update_image(self,image_title,image_category=None):
        self.image_title=image_title if image_title else self.image_category
        
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod 
    def copy_image(cls,image_url):
        pyperclip.copy(image_url)
    
    def delete_image(self):
        self.delete()
        
    @classmethod
    def search_by_category(cls,category):
        images = cls.objects.filter(image_category__icontains=category)
        return images
    
    @classmethod
    def filter_by_location(cls,location):
        image_location = IMage.objects.filter(location__title=location).all()
    
        
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    image_title = models.CharField(max_length=30)
    description= models.TextField(max_length=100)
    
class Location(models.Model):
    place = models.CharField(max_length=200)
    
    def __str__(self):
        return f'place: {self.place}'
    
    

