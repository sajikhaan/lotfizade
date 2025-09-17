from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=255, blank=True)  # اضافه شد
    cover = models.ImageField(upload_to='blog/covers/', blank=True, null=True)  # اضافه شد
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.slug])
