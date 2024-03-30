from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, "photo/gallery.html")

def viewPhoto(request, pk):
    return render(request, "photo/photo.html")

def addPhoto(request):
    return render(request, "photo/add.html")