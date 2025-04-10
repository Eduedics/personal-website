from django.db import models
import uuid

class Projects(models.Model):
    id = models.UUIDField(editable=False,unique=True,primary_key=True)
    image =models.ImageField(blank=True,null=True)
    title = models.CharField(blank=True,null=True,max_length=200)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    preview_url = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
class description(models.Model):
    id = models.UUIDField(editable=False,unique=True,primary_key=True)
    description = models.TextField(blank=True,null=True)
    skillset = models.CharField(blank=True,null=True,max_length=200)
    
    def __str__(self):
        return self.description
    
class Tag(models.Model):
    f_name= models.CharField(blank=True,null=True,max_length=200)
    l_name= models.CharField(blank=True,null=True,max_length=200)
    image =models.ImageField(blank=True,null=True)
    title = models.CharField(blank=True,null=True,max_length=200)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.f_name
    
