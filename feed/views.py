from django.shortcuts import render,redirect
from .models import Post
from accounts.models import Profile
from .forms import PostForm


def homefeed(request):

    if request.user.is_authenticated:

        profiles = Profile.objects.all().exclude(user=request.user)

        posts = Post.objects.all()
        
        form = PostForm()

        if request.method == "POST":
            form = PostForm(request.POST)
            
            if form.is_valid():
                thepost = form.save(commit=False)
                thepost.user = request.user
                thepost.save()
            return redirect('feed')
        
        return render(request, 'feed/homefeed.html',{'posts':posts,'form':form,'profiles':profiles})
    else:
        return redirect('login')

def editpost(request,pk):

    post = Post.objects.get(pk=pk)

    form = PostForm(instance=post)

    if request.method == 'POST':

        if request.user == post.author.user:

            form = PostForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
                return redirect('feed')
        
    return render(request, 'feed/editpost.html',{'form':form})

def deletepost(request,pk):

    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('feed')

    return render(request, 'feed/deletepost.html', {'post':post})