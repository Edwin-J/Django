from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.models import User

user = User.objects.get(username='admin')
def post_list(request):
    posts=Post.objects.all()
    return render(request, 'firstapp/home.html',{'posts':posts})

def static(request):
    return render(request, 'firstapp/' + request + '.html')

def main(request) :
    return render(request, 'firstapp/main.html')

def introduce(request) :
    return render(request, 'firstapp/introduce.html')

def study(request) :
    return render(request, 'firstapp/study.html')


def base(request) :
    return render(request, 'firstapp/base.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.published_date = timezone.now()
            post.save()
            return redirect('../../', pk=post.pk)
    else:
        form = PostForm()
        
    return render(request, 'firstapp/post_edit.html', {'form': form})
    

def post_edit(request, post_id) :
    post = get_object_or_404(Post, pk = post_id)
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit = False)
            post.author = user
            post.published_date = timezone.now()
            post.save()
            return redirect('firstapp.views.post_detail', post_id = post.pk)
    else :
        form = PostForm(instance = post)

    return render(request, 'firstapp/post_edit.html', {'form' : form})
