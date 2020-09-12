from django.db import models

# Create your models here.

class Photo(models.Model):
    name=models.CharField(max_length=20)
    file = models.ImageField(upload_to="images")
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name