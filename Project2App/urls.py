from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newUser/', views.newUser, name='newUser'),
    path('search/', views.search, name='search'),
    path('createWiki/', views.createWiki, name='createWiki'),
    path('personalWiki/', views.personalWiki, name='personalWiki'),
    path('details/<int:id>/', views.details, name='details'),
    path('relatedContent/<int:id>', views.relatedContent, name='relatedContent'),
    path('editPost/<int:contID>/', views.editPost, name='editPost'),
    path('deletePost/<int:contID>/', views.deletePost, name='deletePost'),
    path('editRelated/<int:relID>/', views.editRelated, name='editRelated'),
    path('deleteRelated/<int:relID>/', views.deleteRelated, name='deleteRelated'),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
]
