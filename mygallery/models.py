
from unicodedata import category
from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    image_category = models.CharField(max_length=30)
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()    
        
    def get_category_id(cls,id):
        category = Category.object.get(pk=id)
        return category
    
    def __str__(self):
        return self.image_category
    
class Location(models.Model):
    image_location = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()
        
    # def delete_location(self): 
    #     self.delete()
        
    # def get_location_id(cls,id):
    #     location = Location.object.get(pk=id)
    #     return location   
    
    # def __str__(self):
    #     return self.image_location        

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
    
    @classmethod
    def get_all_images(cls):
        all_img=Image.objects.all()
        return all_img
    
    @classmethod
    def filter_by_location(cls,id):
        images = Image.objects.filter(location_id=id)
        return images
    
    @classmethod
    def search_by_category(cls, search_term):
        image= cls.objects.filter(category__icontains=search_term)
        return image
    
    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(img_name=current_value).update(img_name=new_value)
        return fetched_object
    
    

        
        
        
        
      
