from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/', views.shopping, name='shopping'),
    url(r'^search-new/', views.search_new, name='search_new'),
    url(r'^search-basic/', views.search_basic, name='search_basic'),
    url(r'^search-sale/', views.search_sale, name='search_sale')
]