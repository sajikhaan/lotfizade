from django import forms
from services.models import Service
from gallery.models import GalleryPhoto
from blog.models import BlogPost

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'slug', 'short_description', 'content', 'cover', 'featured']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = ['title', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'summary', 'content', 'cover']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
