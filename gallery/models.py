from django.db import models

class GalleryPhoto(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/photos/')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
