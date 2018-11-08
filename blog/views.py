from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def get_index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {'posts': posts})
    
def read_post(request,id):
    post = get_object_or_404(Post, pk=id)

    return render(request, "blog/read_post.html",{'blog_post':post})
    
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect(read_post, id)
    else:        
        form=PostForm(instance=post)
        return render(request, "blog/post_form.html", {'form': form }) 

def write_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        post=form.save()
        return redirect(read_post, post.id)
    else:        
        form=PostForm()
        return render(request, "blog/post_form.html", {'form': form })    