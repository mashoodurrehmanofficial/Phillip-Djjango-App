from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete,post_save,pre_save
from django.dispatch.dispatcher import receiver
from datetime import datetime

 
 
class Tweet_Table(models.Model):
    username            = models.CharField(max_length=10000,blank=True,default='') 
    profile_image_url   = models.CharField(max_length=10000,blank=True,default='') 
    text                = models.CharField(max_length=10000,blank=True,default='') 
    created_at          = models.DateField(blank=True,null=True)  
    retweet_count       = models.IntegerField(default=0, blank=True,null=True)  
    like_count          = models.IntegerField(default=0, blank=True,null=True) 
    imported            = models.BooleanField(default=False) 
    user                = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return self.username
 
 
class Imported_Tweet_Table(models.Model):
    username        = models.CharField(max_length=10000,blank=True,default='') 
    text            = models.CharField(max_length=10000,blank=True,default='') 
    created_at      = models.DateField(blank=True,null=True)  
    retweet_count   = models.IntegerField(default=0, blank=True,null=True)  
    like_count      = models.IntegerField(default=0, blank=True,null=True) 
    imported        = models.BooleanField(default=False) 
    user            = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return self.username
 