from django.db import models
from django.db.models.functions import Now
from django.contrib.auth.models import AbstractUser

class Blogs(models.Model):
      title = models.CharField(max_length=100,null=True)
      slug = models.CharField(max_length=255,null=True)
      author = models.CharField(max_length=100,null=True)
      content = models.CharField(max_length=255,null= True)
      categories = models.CharField(max_length=255,default='Draft')
      tags = models.CharField(max_length=255,default='trending')
      publication_date = models.DateField(auto_now=True)
        

        
class User(AbstractUser):
      ROLE_CHOICES = (
           ('user','User'),
           ('admin','Admin'))    
      role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')

class Permission(models.Model):
      ROLE_CHOICES = User.ROLE_CHOICES
      role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')
      can_view = models.BooleanField(default=True)
      can_edit = models.BooleanField(default=False)
      can_post = models.BooleanField(default=False)
       
       
      def can_user_post(self):
          return self.can_post
      
      def can_user_view(self):
          return self.can_view
      
      def can_user_edit(self):
          return self.can_edit
       
   
    