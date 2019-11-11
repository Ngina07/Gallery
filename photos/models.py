from django.db import models
from django.db.models import Q

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

class Image(models.Model):
    title=models.CharField(max_length=50)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls,Image):
        cls.objects.filter(image = image).delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()

        return images

    @classmethod
    def search_image(cls,search_term):
        
        images = cls.objects.filter(Q(categories__category=search_term) | Q(title__icontains=search_term))
        return images




    






