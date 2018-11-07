from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Post, Comment
from .forms import UserLoginForm, UserRegisterForm, PostUploadForm
from django.conf import settings


# Create your views here.

@ensure_csrf_cookie
def loginView(request):
    print(request.user)
    if not request.user.id == None:
        return redirect('project:homepage')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('project:homepage')
            else:
                error_message = 'User is inactive.'
                return render(request, 'project/login.html', {'error_message': error_message, 'form': form})
        error_message = 'Invalid Login'
        return render(request, 'project/login.html', {'error_message': error_message, 'form': form})
    if request.method == 'GET':
        form = UserLoginForm(None)
        return render(request, 'project/login.html', {'form': form})


def registerView(request):
    if not request.user.id == None:
        return redirect('project:homepage')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('project:login')
        error_message = 'Invalid Form'
        return render(request, 'project/register.html', {'form': form, 'error_message': error_message})
    if request.method == 'GET':
        form = UserRegisterForm(None)
        return render(request, 'project/register.html', {'form': form})


@login_required
def homePage(request):
    posts = Post.objects.exclude(author=request.user).order_by('-time')
    return render(request, 'project/homepage.html', {'posts': posts})


@login_required
def postDetail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post).all().order_by('time')
    return render(request, 'project/postDetail.html', {'post': post, 'comments': comments})


@login_required
def like(request, pk):
    post = get_object_or_404(Post, id=pk)
    user = request.user
    try:
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
    except (KeyError, Post.DoesNotExist):
        return JsonResponse({'success': False})
    return JsonResponse({'success': True})


@login_required
def uploadPost(request):
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('project:detail', post.id)
        return render(request, 'project/upload.html', {'form': form})
    else:
        form = PostUploadForm(None)
        return render(request, 'project/upload.html', {'form': form})



@login_required
def uploadComment(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        post = get_object_or_404(Post, id=pk)
        content = request.POST.get('comment')
        comment = Comment(author=user, text=content, post=post)
        comment.save()
    return redirect('project:detail', pk=pk)


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).all().order_by('-time')
    return render(request, 'project/profile.html', {'user': user, 'posts': posts})


@login_required
def logout_view(request):
    logout(request)
    return redirect('project:homepage')