from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    description = models.TextField(null=True)
    img_url = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"