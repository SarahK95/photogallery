from django.db import models


# Create your models here.
class Categorys(models.Model):
    image_category = models.CharField(max_length=100, blank=True, null=True)
    
    
    def __str__(self):
        return self.image_category
    
class Locations(models.Model):
    location_name = models.CharField(max_length=100, blank=True, null=True)
    
    
    def __str__(self):
        return self.location_name        

class Images(models.Model):
    img_name =models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to ='photos/')
    location = models.ForeignKey(Locations, null=True, blank=True,on_delete=models.CASCADE ) 
    category = models.ForeignKey(Categorys,  null=True, blank=True, on_delete=models.CASCADE)
   
   
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
        img = Images.objects.get(id=id)
        return img
    
    @classmethod
    def get_all_images(cls):
        all_images=Images.objects.all()
        return all_images
    
    @classmethod
    def filter_by_location(cls,id):
        images = Images.objects.filter(location_id=id)
        return images
    
    @classmethod
    def search_by_category(cls, search_term):
        image= cls.objects.filter(category__icontains=search_term)
        return image
    
    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Images.objects.filter(img_name=current_value).update(img_name=new_value)
        return fetched_object
    
    

        
        
        
        
      
