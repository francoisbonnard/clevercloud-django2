from django.urls import path
from . import views

# to import stati files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.gallery, name='gallery'),
    path('photo/<str:pk>',views.viewPhoto, name='photo'),
    path('add/',views.addPhoto, name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
