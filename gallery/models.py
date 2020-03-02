from django.db import models

# Create your models here.
class Image(models.Model):
    image_title = models.CharField(max_length=60)
    image_description = models.TextField(max_length=500)
    image_category = models.CharField(max_length=30,blank=True)
    
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
    def search_by_category(cls,category):
        images = cls.objects.filter(image_category__icontains=category)
        return images
    
        
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.title
    
    

