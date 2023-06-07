from django.db import models

# Create your models here.
#event  event
class Eventuser(models.Model):
    event_user_name=models.CharField(max_length=50)
    event_user_email = models.EmailField()
    def __str__(self):
        return self.event_user_name

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_desc = models.TextField()
    slug = models.CharField(max_length=50)
    time = models.DateTimeField('date_published',auto_now_add=True)
    event_createdby=models.CharField(max_length=50,default='')
    event_participant = models.ManyToManyField(Eventuser)    
    def __str__(self):
        return self.event_name




