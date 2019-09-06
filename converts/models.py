from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('home')
