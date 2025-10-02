from django.shortcuts import render
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import UsercreationForm
from django.contrib import messages

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/home.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
            messages.success(request, 'Tweet created successfully!')
        else:
            messages.error(request, 'Content cannot be empty.')
    return render(request, 'tweets/create_tweet.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

