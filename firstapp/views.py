from django.shortcuts import render
from .models import Post
from .forms import PostForm


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

def post_new(request) :
    form = postForm()
    return render(request, 'firstapp/post_edit.html', {'form' : form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'firstapp/post_edit.html', {'form': form})

# Create your views here.
