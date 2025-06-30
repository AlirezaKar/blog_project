from django.shortcuts import render, redirect
from .forms import CommentForm, LoginForm
from .models import Article, Comment, User

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    articles = Article.objects.all()
    data = {
        'articles':articles
    }
    return render(request=request, template_name='blog/index.html', context=data)

@login_required(login_url='/login/')
def detail(request, id):
    if request.method == 'POST':
        post = Article.objects.get(id = id)
        data = CommentForm(request.POST)
        if data.is_valid():
            form_data = data.cleaned_data
            username = form_data.get("email").split("@")[0]
            try:
                user = User.objects.get(username=username)
            except:
                user = User.objects.create(username=username, email=form_data.get("email"))

            comment = Comment.objects.create(user=user, comment=form_data.get("content"), content=post)
        else:
            form = CommentForm()
            context = {'post':post, 'form':form}
            return render(request=request, template_name='blog/detail.html', context=context)
    else:
        post = Article.objects.get(id = id)
        form = CommentForm()
        comments = Comment.objects.filter(content=post)
        context = {'post':post, 'form':form, 'comments':comments}
        return render(request=request, template_name='blog/detail.html', context=context)

    try:
        post = Article.objects.get(id = id)
        comments = post.comment.all()
        form = CommentForm()
        context = {"post":post, "form": form, "comment":comments}
        return render(request=request,template_name="blog/detail.html", context=context)
    except:
        return redirect(index)


def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        data = LoginForm(request.POST)
        if data.is_valid():
            form_data = data.cleaned_data
            username = form_data.get("username")
            password = form_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect(profile_view)
            else:
                messages.error(request=request, message="invalid username or password!") #FIXME: doesn't show 
                form = LoginForm()
                context = {'form':form}
                return render(request=request, template_name='registrations/login.html', context=context)
                #TODO: make them be redirected to registration page if user is not available            
    else:
        form = LoginForm()
        context = {'form':form}
        return render(request=request, template_name='registrations/login.html', context=context)

# TODO: a more   advanced and customizable logout view (must delete the session id in order to logout)
# @login_required
# def logout(request):
#     return redirect(login_view)

@login_required
def profile_view(request):
    return render(request=request, template_name='registrations/profile.html')

def resume_view(request):
    posts_count = len(Article.objects.all())
    context = {'posts_count':posts_count}
    return render(request=request, template_name='blog/resume.html', context=context)

def contacts_view(request):
    return render(request=request, template_name='blog/contacts.html')