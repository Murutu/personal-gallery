from django.db import models

# Create your models here.
class Image(models.Model):
    image_title = models.CharField(max_length=30)
    image_description = models.TextField(max_length=500)
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.title
    
    

