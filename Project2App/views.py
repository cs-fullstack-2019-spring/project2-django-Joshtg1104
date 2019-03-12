from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "Project2App/index.html")


def createWiki(request):
    return render(request, "Project2App/createWiki.html")


def personalWiki(request):
    return render(request, "Project2App/personalWiki.html")


def relatedContent(request):
    return render(request, "Project2App/relatedContent.html")


def editPost(request):
    return render(request, "Project2App/editPost.html")

def deletePost(request):
    return render(request, "Project2App/deletePost.html")

def editRelated(request):
    return render(request, "Project2App/editRelated.html")

def deleteRelated(request):
    return render(request, "Project2App/deleteRelated.html")
