from unicodedata import category
from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    img_name =models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
   
    class Meta:
        ordering = ['img_name']
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()  
        
    def __str__(self):
           return self.img_name      
        
    @classmethod  
    def get_image_by_id(cls, id):
        img = Image.objects.get(id=id)
        return img
    
    # @classmethod
    # def get_all_images(cls):
    #     all_img=Image.objects.all()
    #     return all_img
    
    # @classmethod
    # def filter_by_location(cls,id):
    #     images = Image.objects.filter(location_id=id)
    #     return images
    
    # @classmethod
    # def search_by_category(cls, search_term):
    #     image= cls.objects.filter(category__image_category__icontains=search_term)
    #     return image_category
        
        
      
