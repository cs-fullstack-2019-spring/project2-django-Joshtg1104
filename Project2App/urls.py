from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newUser/', views.newUser, name='newUser'),
    path('createWiki/', views.createWiki, name='createWiki'),
    path('personalWiki/', views.personalWiki, name='personalWiki'),
    path('details/<int:id>/', views.details, name='details'),
    path('relatedContent/', views.relatedContent, name='relatedContent'),
    path('editPost/', views.editPost, name='editPost'),
    path('deletePost/', views.deletePost, name='deletePost'),
    path('editRelated/', views.editRelated, name='editRelated'),
    path('deleteRelated/', views.deleteRelated, name='deleteRelated'),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
]
