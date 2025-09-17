from django.shortcuts import render
from services.models import Service
from gallery.models import GalleryPhoto
from blog.models import BlogPost

def home(request):
    featured_services = Service.objects.filter(featured=True)[:4]
    recent_photos = GalleryPhoto.objects.order_by('-uploaded')[:6]
    recent_posts = BlogPost.objects.filter(published=True).order_by('-created')[:3]
    return render(request, 'home.html', {
        'featured_services': featured_services,
        'recent_photos': recent_photos,
        'recent_posts': recent_posts,
    })
