from django.urls import path
from . import views
from django.conf import settings


urlpatterns= [

    path('',views.home_page_view,name='home_page'),
    path('TopGitHubRepos',views.repo_page_view,name='repo_page'),
]