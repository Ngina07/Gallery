from django.db import models

class Location(models.Model):
    location = models.charField(max_length=100)

    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ['location']

        

