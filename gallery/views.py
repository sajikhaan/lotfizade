from django.views.generic import ListView
from .models import GalleryPhoto

class GalleryListView(ListView):
    model = GalleryPhoto
    template_name = 'gallery/list.html'
    context_object_name = 'photos'
