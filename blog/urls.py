from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category'),
    path('article/<int:article_id>/', article_detail_view, name='article_detail'),

    path('about_us/', about_us_page_view, name='about_us'),
    path('our_team/', our_teams_page_view, name='our_team'),
    path('services/', our_services_page_view, name='services'),

    path('add_article/', add_article, name='add_article')
]
