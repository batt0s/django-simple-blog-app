from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Article, Comment

def index(request):

    last_article = Article.objects.first()

    if last_article:

        return render(request, "index.html", {"article":last_article})

    return render(request, "index.html")


def about(request):

    return render(request, "about.html")


def articles(request):

    keyword = request.GET.get("keyword")

    if keyword:

        articles = Article.objects.filter(title__contains=keyword)

        return render(request, "articles.html", {"articles":articles})

    articles = Article.objects.all()

    return render(request, "articles.html", {"articles":articles})

@login_required(login_url="user:login")
def create_article(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():

        newArticle = form.save(commit=False)
        newArticle.author = request.user
        newArticle.save()

        messages.success(request, "Article added successfully.")
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "add_article.html", context)


@login_required(login_url="user:login")
def delete(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    article.delete()

    messages.success(request, "Article deleted successfully.")
    return redirect("user:dashboard")



@login_required(login_url="user:login")
def edit(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    form = ArticleForm(request.POST or None, instance=article)

    if form.is_valid():

        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Article updated successfully.")
        return redirect("index")

    return render(request, "update.html", {'form':form})



def detail(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    comments = article.comments.all()

    context = {
        "article": article,
        "comments": comments
    }

    return render(request, 'article.html', context)



def addComment(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":

        comment_author = request.POST.get("comment_author")
        comment_author_email = request.POST.get("comment_author_email")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_author_email=comment_author_email, comment_content=comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail", kwargs={"article_id":article_id}))