from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    git_page = models.URLField()
    viewer = models.URLField(default='https://blabubaer.github.io/start-it-module1/')

    def __str__(self):
      return self.title
