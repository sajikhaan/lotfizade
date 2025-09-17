from django.shortcuts import render, redirect, get_object_or_404
from services.models import Service
from gallery.models import GalleryPhoto

from blog.models import BlogPost
from .forms import ServiceForm, PhotoForm, PostForm

# داشبورد
def admin_dashboard(request):
    context = {
        'services': Service.objects.all(),
        'photos': GalleryPhoto.objects.all(),
        'posts': BlogPost.objects.all()
    }
    return render(request, 'admin_panel/dashboard.html', context)

# ----------------- خدمات -----------------
def add_service(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:dashboard')
    return render(request, 'admin_panel/form.html', {'form': form, 'title': 'افزودن خدمت'})

def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:dashboard')
    return render(request, 'admin_panel/form.html', {'form': form, 'title': 'ویرایش خدمت'})

def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('admin_panel:dashboard')

# ----------------- عکس -----------------
def add_photo(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:dashboard')
    return render(request, 'admin_panel/form.html', {'form': form, 'title': 'افزودن عکس'})

def delete_photo(request, pk):
    photo = get_object_or_404(GalleryPhoto, pk=pk)
    photo.delete()
    return redirect('admin_panel:dashboard')

# ----------------- مقاله -----------------
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:dashboard')
    return render(request, 'admin_panel/form.html', {'form': form, 'title': 'افزودن مقاله'})

def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:dashboard')
    return render(request, 'admin_panel/form.html', {'form': form, 'title': 'ویرایش مقاله'})

def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('admin_panel:dashboard')
