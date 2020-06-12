from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import models, login, logout, authenticate

from .forms import LoginForm, RegisterForm

from article.models import Article, Comment

def registerUser(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        password = form.cleaned_data.get("password")

        newUser = models.User(username=username, email=email, first_name=first_name, last_name=last_name)
        newUser.set_password(password)
        newUser.save()

        messages.success(request, "You registered successfully.")
        return redirect("user:login")

    context = {
        "form": form
    }

    return render(request, "register.html", context)


def loginUser(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:

            messages.error(request, "Username or password entered incorrectly.")
            return redirect("user:login")

        messages.success(request, "You are logged in successfully.")
        login(request, user)
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "login.html", context)

@login_required(login_url="user:login")
def logoutUser(request):

    logout(request)
    messages.info(request, "You are logged out.")
    return redirect("user:login")

@login_required(login_url="user:login")
def dashboard(request):

    articles = Article.objects.filter(author=request.user)

    comments = []

    for article in articles:

        article_comments = article.comments.all()

        for comment in article_comments:

            comments.append(comment)

    context = {
        "articles": articles,
        "comments": comments
    }

    return render(request, "dashboard.html", context)


def userIndex(request):

    return redirect('user:dashboard')