from django.shortcuts import render,redirect
from .models import Post, Comments 
from accounts.models import Profile
from .forms import PostForm, CommentForm


def homefeed(request):

    if request.user.is_authenticated:

        profiles = Profile.objects.all().exclude(user=request.user)

        profile = Profile.objects.get(user=request.user)
            
        following = profile.following.all()
        
        posts = Post.objects.filter(author__in=following)
        
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

def postlike(request, pk):

    posts = Post.objects.get(pk=pk)

    posts_likes = posts.likes.all()
    posts_me_liked = posts.likes.filter(id=request.user.id)

    
    if posts_me_liked.exists():

        posts.likes.remove(request.user)

    else:

        posts.likes.add(request.user)

    return redirect('detail_post', pk=pk)


def detailpost(request, pk):

    posts = Post.objects.get(pk=pk)

    posts_likes = posts.likes.all()
    
    posts_me_liked = posts.likes.filter(id=request.user.id)
    
    comments = Comments.objects.filter(post=posts)
    
    form = CommentForm()

    if request.method == "POST":
        posts = Post.objects.get(pk=pk)
        
        form = CommentForm(request.POST)

        if form.is_valid():
            createdcomment = form.save(commit=False)
            createdcomment.post = Post.objects.get(pk=pk)
            createdcomment.commentor = request.user
            createdcomment.save()
        return redirect('feed')

    return render(request, 'feed/detailpost.html', {'posts':posts,'comments':comments,'form':form,'posts_likes':posts_likes,'posts_me_liked':posts_me_liked})


def editpost(request,pk):

    post = Post.objects.get(pk=pk)

    form = PostForm(instance=post)

    if request.method == 'POST':

        if request.user == post.author :

            form = PostForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
                return redirect('feed')
        
    return render(request, 'feed/editpost.html',{'form':form})

def deletepost(request,pk):

    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        
        if request.user == post.author:

            post.delete()
            return redirect('feed')

    return render(request, 'feed/deletepost.html', {'post':post})

