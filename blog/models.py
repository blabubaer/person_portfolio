from django.db import models

class Blog(models.Model):
   title = models.CharField(max_length=255)
   pub_date = models.DateTimeField(auto_now=None,auto_now_add=None)
   body = models.TextField()
   image = models.ImageField(upload_to='images')
