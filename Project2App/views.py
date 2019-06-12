from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewUserForm, RelatedContentForm, WikiForm, NewUserModel, RelatedContentModel, WikiModel
from django.db.models import Q


# Create your views here.


# Displays all wikis on the main home page
def index(request):
    allWiki = WikiModel.objects.all()
    context = {
        "allWiki": allWiki
    }
    return render(request, "Project2App/index.html", context)

# allows the NewUserForm to appear on its own page when the new User button on the index html is clicked
def newUser(request):
    userform = NewUserForm(request.POST or None)
    if request.method == "POST":
        if userform.is_valid():
            # saves the form if it is valid
            userform.save()

            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            return redirect('index')
    context = {
        "errors": userform.errors,
        "userform": userform
    }
    return render(request, "Project2App/newUser.html", context)

# allows the wikiform to appear when the Create Wiki link is selected
def createWiki(request):
    # creates a variable for the WikiForm
    wikiform = WikiForm(request.POST)
    # makes it so that this only happens if a user is signed in
    if request.user.is_authenticated:
        user = NewUserModel.objects.get(username=request.user)
        if wikiform.is_valid():
            print(request.POST)
            # if the form is valid then a new wiki entry will be created
            WikiModel.objects.create(title=request.POST["title"], body=request.POST["body"],
                                     image=request.FILES["image"], wikiForeignKey=user)
            return redirect('index')
    # if the a user is not logged in then this will happen
    context = {
        "wiki": wikiform,
        "errors": wikiform.errors
    }
    return render(request, "Project2App/createWiki.html", context)

# allows the details of specific wikis articles to appear on their own page
def details(request, id):
    # a variable created to help individualize the articles
    detailedWiki = get_object_or_404(WikiModel, pk=id)
    # filters the articles using a foreignkey
    related = RelatedContentModel.objects.filter(relatedForeignKey=detailedWiki)
    context = {
        "detailedWiki": detailedWiki,
        "relatedItems": related
    }
    return render(request, "Project2App/details.html", context)

# a function that filters out any articles not created by the user if the Personal Wikis link is selected
def personalWiki(request):
    # this happens if there is a user logged in
    if request.user.is_authenticated:
        wikiUser = NewUserModel.objects.get(username=request.user)
        userWikis = WikiModel.objects.filter(wikiForeignKey=wikiUser)
    else:
        # if a user is not logged in then this happens
        userWikis = ""
    context = {
        "userWikis": userWikis
    }
    return render(request, "Project2App/personalWiki.html", context)

# allows for related content to be created and appear on detailed pages
def relatedContent(request, id):
    relatedform = RelatedContentForm(request.POST)
    # this will only happen if a user is logged in
    if request.user.is_authenticated:
        detailedWiki = get_object_or_404(WikiModel, pk=id)
        if relatedform.is_valid():
            print(request.POST)
            RelatedContentModel.objects.create(title=request.POST["title"], body=request.POST["body"],
                                               image=request.FILES["image"], relatedForeignKey=detailedWiki)
            return redirect('details', id)
    # otherwise this happens
    context = {
        "related": relatedform,
        "errors": relatedform.errors,
        "id": id,
    }
    return render(request, "Project2App/relatedContent.html", context)

# allows the user to edit wiki entries
def editPost(request, contID):
    editContent = get_object_or_404(WikiModel, pk=contID)
    if request.method == "POST":
        wikiform = WikiForm(request.POST, instance=editContent)
        if wikiform.is_valid():
            # if the form is valid it will be saved
            wikiform.save()
        return redirect('personalWiki')
    wikiform = WikiForm(instance=editContent)
    context = {
        "wikiform": wikiform,
        "contID": contID
    }
    return render(request, "Project2App/editPost.html", context)

# allows the user to delete wiki entries
def deletePost(request, contID):
    deleteContent = get_object_or_404(WikiModel, pk=contID)
    if request.method == "POST":
        # deletes the post
        deleteContent.delete()
        return redirect('personalWiki')
    # otherwise does not delete the wiki entry
    return render(request, "Project2App/deletePost.html", {"delete": deleteContent, "contID": contID})

# allows for related content to be edited by a user
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

# allows the user to delete their related content
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

def search(request):
    lookup = WikiModel.objects.filter(Q(title__contains=request.POST['q']))
    print(lookup)
    context = {
        "results": lookup
    }
    return render(request, "Project2App/searchResults.html", context)
