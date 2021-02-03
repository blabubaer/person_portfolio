from django.db import models

class Blog(models.Model):
   title = models.CharField(max_length=255)
   pub_date = models.DateTimeField(auto_now=None,auto_now_add=None)
   body = models.TextField()
   image = models.ImageField(upload_to='images')

   def summary(self):
      sumary = self.body[:100]
      if len(self.body) > 100:
         return sumary + '...'
      else:
         return self.body

   
   def pub_date_pretty(self):
      return self.pub_date.strftime('%b %e %Y')
   
   def __str__(self):
      return self.title
