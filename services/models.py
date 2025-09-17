from django.db import models
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    short_description = models.CharField(max_length=255)
    content = models.TextField()
    cover = models.ImageField(upload_to='services/covers/')
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', args=[self.slug])
