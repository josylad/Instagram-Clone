from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Location, Image, Category, Comment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, NewsLetterForm, NewCommentForm


# Create your views here.


def index(request):
    date = dt.date.today()
    images = Image.get_images()
    comments = Comment.get_comment()
    location = Location.get_location()
    locations = Location.get_location()
    
    current_user = request.user 
    if request.method == 'POST':
        form = NewCommentForm(request.POST, auto_id=False)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
        return redirect('index')
    else:
        form = NewCommentForm(auto_id=False)

    return render(request, 'index.html', {"date": date, "images":images, "location": location, "locations": locations, "comments":comments, "form": form,})


@login_required(login_url='/accounts/login/')
def search_images(request):
    locations = Location.get_location()
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"images": searched_images, "locations": locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, "locations":locations})


@login_required(login_url='/accounts/login/')
def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        current_user = request.user 
        if request.method == 'POST':
            form = NewCommentForm(request.POST, auto_id=False)
            img_id = request.POST['image_id']
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = current_user
                image = Image.get_image(img_id)
                comment.image = image
                comment.save()
            return redirect('get_image')
        else:
            form = NewCommentForm(auto_id=False)
        
        return render(request, "images.html", {"image":image, "locations":locations, "form":form})
    
    
def location(request, location):
    images = Image.search_by_location(location)
    locations = Location.get_location()
    message = f"{location}"
    return render(request, 'locations.html', {"message":message, "images":images, "locations":locations})


def category(request, category):
    images = Image.get_by_category(category)
    locations = Location.get_location()
    message = f"{category}"
    return render(request, 'category.html', {"message":message, "images":images, "locations":locations})


def navlocation(request):
    
    locations = Location.get_location()

    return render(request, 'navbar.html', {"locations": locations})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.Author = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new-image.html', {"form": form})