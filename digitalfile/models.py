from django.db import models

# Create your models here.
class DigitalFiles(models.Model):
    Name =models.CharField(max_length=300)
    Surname = models.CharField(max_length=300)
    Email = models.EmailField(max_length=254)
    Title = models.CharField(max_length=300)
    Description = models.TextField(blank=True)
    Field = models.CharField(max_length=100)
    Created = models.DateTimeField(auto_now_add=True)
    FileUpload=models.FileField(upload_to='uploads/')


    def __str__(self):
        return self.Title
