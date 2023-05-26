from django.db import models


class Newsitem(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    summary = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/', blank=True)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title
