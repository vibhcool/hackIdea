from django.db import models
from django.utils import timezone


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=120, unique=True)
    pwd= models.CharField(max_length=80)
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.IntegerField(default=0) #simple=0 org=1
    def __str__(self):
        return self.email

class Idea(models.Model):
    """ideas """
    title = models.CharField(max_length=300, unique=True)
    description = models.EmailField(max_length=1200)
    link = models.CharField(max_length=500, default=None)
    prototype_link = models.CharField(max_length=500, default=None)
    user = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    public = models.CharField(max_length=5)
    
    def __str__(self):
        return self.title

class Feedback(models.Model):
    title = models.CharField(max_length=300)
    feedback = models.CharField(max_length=600)
    user = models.CharField(max_length=50)
    feedback_id = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.feedback_id

