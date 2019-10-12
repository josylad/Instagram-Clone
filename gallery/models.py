from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.



class Location(models.Model):
    location = models.CharField(max_length= 255, blank =True)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
      

class Category(models.Model):
    category = models.CharField(max_length= 255)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def get_category(cls):
        categories = cls.objects.all()
        return categories
    
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
    
    def __str__(self):
        return self.category
   
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
class Image(models.Model):
    image_file = models.ImageField(upload_to = 'images/', default='images/beagle.jpg')
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

       
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_images(cls, search_term):
        images = cls.objects.filter(description__icontains=search_term)
        return images
    
    @classmethod
    def search_by_location(cls, location):
        images = cls.objects.filter(location__location=location)
        return images
    
    @classmethod
    def get_by_category(cls, category):
        images = cls.objects.filter(category__category=category)
        return images
    
    @classmethod
    def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return image
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['image_name']
        verbose_name = 'My image'
        verbose_name_plural = 'Images'


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
    
    @classmethod
    def get_comment(cls):
        comments = cls.objects.all()
        return comments
    
    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
        
class Profile(models.Model):
    bio = models.TextField()
    photo = models.ImageField(upload_to = 'images/', blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles
    
    def __str__(self):
        return self.bio
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'