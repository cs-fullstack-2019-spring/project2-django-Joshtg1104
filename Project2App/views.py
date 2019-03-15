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
    related = RelatedContentModel.objects.filter(relatedForeignKey=detailedWiki)
    context = {
        "detailedWiki": detailedWiki,
        "relatedItems": related
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


def relatedContent(request, id):
    relatedform = RelatedContentForm(request.POST)
    if request.user.is_authenticated:
        detailedWiki = get_object_or_404(WikiModel, pk=id)
        if relatedform.is_valid():
            print(request.POST)
            RelatedContentModel.objects.create(title=request.POST["title"], body=request.POST["body"],
                                               image=request.FILES["image"], relatedForeignKey=detailedWiki)
            return redirect('details', id)
    context = {
        "related": relatedform,
        "errors": relatedform.errors,
        "id": id,
    }
    return render(request, "Project2App/relatedContent.html", context)


def editPost(request, contID):
    editContent = get_object_or_404(WikiModel, pk=contID)
    if request.method == "POST":
        wikiform = WikiForm(request.POST, instance=editContent)
        if wikiform.is_valid():
            wikiform.save()
        return redirect('personalWiki')
    wikiform = WikiForm(instance=editContent)
    context = {
        "wikiform": wikiform,
        "contID": contID
    }
    return render(request, "Project2App/editPost.html", context)


def deletePost(request, contID):
    deleteContent = get_object_or_404(WikiModel, pk=contID)
    if request.method == "POST":
        deleteContent.delete()
        return redirect('personalWiki')
    return render(request, "Project2App/deletePost.html", {"delete": deleteContent, "contID": contID})


def editRelated(request, relID):
    editcontent = get_object_or_404(RelatedContentModel, pk=relID)
    wikiID = editcontent.relatedForeignKey.id
    if request.method == "POST":
        relatedform = RelatedContentForm(request.POST, instance=editcontent)

        print(wikiID)
        if relatedform.is_valid():
            relatedform.save()
        return redirect('details', wikiID)
    relatedform = RelatedContentForm(instance=editcontent)
    context = {
        "edit": relatedform,
        "wikiID": wikiID,
        "relID": relID
    }
    return render(request, "Project2App/editRelated.html", context)


def deleteRelated(request, relID):
    deletecontent = get_object_or_404(RelatedContentModel, pk=relID)
    wikiID = deletecontent.relatedForeignKey.id
    if request.method == "POST":
        deletecontent.delete()

        # detailedWiki = get_object_or_404(WikiModel, pk=wikiID)
        # related = RelatedContentModel.objects.filter(relatedForeignKey=detailedWiki)
        # context = {
        #     "detailedWiki": detailedWiki,
        #     "relatedItems": related
        # }
        # return render(request, "Project2App/details.html", context)
        return redirect('details', wikiID)
    return render(request, "Project2App/deleteRelated.html", {"deletecontent": deletecontent, "wikiID": wikiID})
