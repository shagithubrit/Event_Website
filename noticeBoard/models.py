from django.db import models

# Create your models here.
class  AdminNotice(models.Model):
    notice = models.TextField()
    date = models.DateField()

    
