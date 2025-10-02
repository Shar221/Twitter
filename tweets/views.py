from django.shortcuts import render
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import TweetForm

def index(request):
    return HttpResponse("Hello, world. You're at the tweets index.")

def create_tweet(request):
    return HttpResponse("Create a new tweet here.")

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/home.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)  # add request.FILES
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("home")
    else:
        form = TweetForm()
    return render(request, "tweets/create_tweet.html", {"form": form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

