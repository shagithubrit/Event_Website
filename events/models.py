from django.db import models

# Create your models here.
#event  event
class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_desc = models.TextField()
    slug = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.event_name

class Participant(models.Model):
    participant_name = models.CharField(max_length=50)
    participant_email = models.EmailField() 

    def __str__(self):
        return self.participant_name 
    
class Entry(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant)



