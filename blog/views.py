from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

# Create your views here.
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def in_authors(request,id):
    inauthors= is_in_group(request.user, 'authors')

    return render(request, "/base.html",{'is_authors':inauthors})
    
def user_can_edit_post(request, post):
    wrote_the_post = post.author == request.user
    is_editor = is_in_group(request.user, 'editors')
    superuser = request.user.is_superuser
    return wrote_the_post or superuser or is_editor


def get_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, "blog/index.html", {'posts': posts})
    
def read_post(request,id):
    post = get_object_or_404(Post, pk=id)
    post.views +=1
    post.save()
    
    can_edit = user_can_edit_post(request, post)

    return render(request, "blog/read_post.html",{'post':post,'can_edit':can_edit})
    
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        form.save()
        return redirect(read_post, id)
    else:        
        form=PostForm(instance=post)
        return render(request, "blog/post_form.html", {'form': form }) 

@login_required
def write_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        post=form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(read_post, post.id)
    else:        
        form=PostForm()
        return render(request, "blog/post_form.html", {'form': form }) 
        


    
@permission_required('blog.can_publish')
def get_unpublished_posts(request):
    posts = Post.objects.filter(published_date__isnull=True)
    return render(request, "blog/index.html", {'posts': posts})    



@permission_required('blog.can_publish')
def publish_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.published_date = timezone.now()
    post.save()
    return redirect(read_post, post.id)






