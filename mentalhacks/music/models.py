from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Journal(models.Model):
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=50, default='No Title')
    date = models.DateField(auto_now=True)
