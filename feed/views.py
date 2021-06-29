from django.shortcuts import render,redirect
from .models import Post, Comments 
from accounts.models import Profile
from .forms import PostForm, CommentForm
from django.views.generic.base import View

class HomeFeedView(View):

    def get(self,request):
    
        profiles = Profile.objects.all().exclude(user=request.user)
        profile = Profile.objects.get(user=request.user)
        posts = Post.objects.filter(author__in=profile.following.all())
        
        search_text = request.GET.get('search_box', None)

        if search_text:
            posts = Post.objects.filter(title__contains=search_text)

        return render(request, 'feed/homefeed.html',{'posts':posts,'form':PostForm(),'profiles':profiles})
    
    def post(self,request):

        form = PostForm(data=request.POST)
        
        if form.is_valid():

            thepost = form.save(commit=False)
            thepost.author = self.request.user 
            thepost.save()
        
        return redirect('feed')

class DetailPostView(View):

    def get(self,request,pk):

        posts = Post.objects.get(pk=pk)

        posts_likes = posts.likes.all() 
    
        posts_me_liked = posts.likes.filter(id=request.user.id)
    
        comments = Comments.objects.filter(post=posts)
    
        form = CommentForm()

        return render(request, 'feed/detailpost.html', {'posts':posts,'comments':comments,'form':form,'posts_likes':posts_likes,'posts_me_liked':posts_me_liked})
    
    def post(self, request, pk):

        posts = Post.objects.get(pk=pk)
        
        form = CommentForm(request.POST)

        if form.is_valid():
            createdcomment = form.save(commit=False)
            createdcomment.post = Post.objects.get(pk=pk)
            createdcomment.commentor = request.user
            createdcomment.save()
        return redirect('detail_post', pk=pk)


class EditPostView(View):

    def get(self,request,pk):

        post = Post.objects.get(pk=pk)

        form = PostForm(instance=post)

        return render(request,'feed/editpost.html',{'post':post,'form':form})
    
    def post(self,request,pk):

        post = Post.objects.get(pk=pk)
        form = PostForm()
        
        if self.request.user == post.author:
            
            form = PostForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
                return redirect('feed')

        return render(request,'feed/editpost.html',{'post':post,'form':form})
class DeletePostView(View):
    
    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'feed/deletepost.html', {'post':post})
    
    def post(self,request,pk):
        post = Post.objects.get(pk=pk)
        if request.user == post.author:
            post.delete()
            return redirect('feed')


def postlike(request, pk):

        posts = Post.objects.get(pk=pk)

        posts_me_liked = posts.likes.filter(id=request.user.id)
        
        if posts_me_liked.exists():

            posts.likes.remove(request.user)

        else:

            posts.likes.add(request.user)

        return redirect('detail_post', pk=pk)