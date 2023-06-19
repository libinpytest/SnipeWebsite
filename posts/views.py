from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post
from .forms import PostForm

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'cancel_url': 'posts'  # Add the cancel URL here
    }
    return render(request, 'create_post.html', context)

@login_required
@user_passes_test(is_admin)
def update_post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
        'cancel_url': 'posts'  # Add the cancel URL here
    }
    return render(request, 'update_post.html', context)

@login_required
@user_passes_test(is_admin)
def delete_post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    
    context = {
        'post': post,
        'cancel_url': 'posts'  # Add the cancel URL here
    }
    return render(request, 'delete_post.html', context)


def view_post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
