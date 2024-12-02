from django.db import models

# Create your models here.

class Data(models.Model):
    image = models.ImageField(upload_to="myimage")
    description = models.TextField()
    category = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.category 
    
class Datareceipe(models.Model):
    image = models.ImageField(upload_to="myimage2")
    description = models.TextField()
   
    def __str__(self):
        return self.category
    

class UserData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confpw = models.CharField(max_length=100)   

