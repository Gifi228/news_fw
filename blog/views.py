from django.shortcuts import render, redirect

from .models import *
from .forms import ArticleForm

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)



def category_page_view(request, category_id):
    # filter() --- брать по условию
    articles = Article.objects.filter(category=category_id)
    trends = Article.objects.all().order_by('views')
    category = Category.objects.get(id=category_id)

    context = {
        "title": f"Катагория: {category.title}",
        "articles": articles,
        "trends": trends,
        "category_name": category.title
    }

    return render(request, "blog/category_page.html", context)


def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last = Article.objects.all().order_by('-created_at')

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "last_articles": last,
    }

    return render(request, "blog/article_detail.html", context)



def about_us_page_view(request):
    return render(request, "blog/about_us.html")


def our_teams_page_view(request):
    return render(request, "blog/our_team.html")


def our_services_page_view(request):
    return render(request, "blog/services.html")

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', article.id)
    else:
        form = ArticleForm()

    context = {
        "title": "Добавить статью",
        "form": form
    }

    return render(request, 'blog/add_article.html', context)






