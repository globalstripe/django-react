from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    description = models.TextField(default='')
    author = models.TextField(default='')
    video = models.URLField(default='')
    thumb = models.URLField(default='')


    def __str__(self):
        return self.title
