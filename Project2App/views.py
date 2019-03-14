from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewUserForm, RelatedContentForm, WikiForm, NewUserModel, RelatedContentModel, WikiModel


# Create your views here.

def index(request):
    allWiki = WikiModel.objects.all()
    context = {
        "allWiki": allWiki
    }
    return render(request, "Project2App/index.html", context)


def newUser(request):
    userform = NewUserForm(request.POST or None)
    if request.method == "POST":
        if userform.is_valid():
            userform.save()
            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            return redirect('index')
    context = {
        "errors": userform.errors,
        "userform": userform
    }
    return render(request, "Project2App/newUser.html", context)


def createWiki(request):
    wikiform = WikiForm(request.POST)
    if request.user.is_authenticated:
        user = NewUserModel.objects.get(username=request.user)
        if wikiform.is_valid():
            print(request.POST)
            WikiModel.objects.create(title=request.POST["title"], body=request.POST["body"],
                                     image=request.FILES["image"], wikiForeignKey=user)
            return redirect('index')
    context = {
        "wiki": wikiform,
        "errors": wikiform.errors
    }
    return render(request, "Project2App/createWiki.html", context)


def details(request, id):
    detailedWiki = get_object_or_404(WikiModel, pk=id)
    context = {
        "detailedWiki": detailedWiki
    }
    return render(request, "Project2App/details.html", context)


def personalWiki(request):
    if request.user.is_authenticated:
        wikiUser = NewUserModel.objects.get(username=request.user)
        userWikis = WikiModel.objects.filter(wikiForeignKey=wikiUser)
    else:
        userWikis = ""
    context = {
            "userWikis": userWikis
        }
    return render(request, "Project2App/personalWiki.html", context)


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
