from django.db import models

#plugin
from datetime import datetime

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        
		return self.username