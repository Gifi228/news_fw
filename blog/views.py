from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


from .models import *
from .forms import *

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


def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()


            return redirect('login')
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = RegistrationUserForm()

        context = {
            "title": "Регистрация пользователя",
            "form": form
        }

        return render(request, "blog/register.html", context)

def login_user_view(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                # TODO: ERROR MESSAGE
                pass
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = LoginUserForm()

    context = {
        "title": "Войти в аккаунт",
        "form": form
    }

    return render(request, "blog/login.html", context)

def logout_user_view(request):
    logout(request)
    return redirect('index')



def update_article_view(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        form = ArticleForm(instance=article,
                           data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
        else:
            # TODO: ERROR MESSAGE
            return redirect("update_article", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "title": "Изменить статью",
        "form": form
    }

    return render(request, "blog/add_article.html", context)


def article_delete(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('index')

    context = {
        "title": "Удаление статьи",
        "article": article
    }

    return render(request, "blog/delete_article.html", context)


def profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "user": user,
        "profile": profile,
        "title": "Профиль пользователя"
    }

    return render(request, "blog/profile.html", context)

