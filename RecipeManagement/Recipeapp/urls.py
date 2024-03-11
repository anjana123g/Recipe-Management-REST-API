"""
URL configuration for RecipeManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Recipeapp import views
app_name="Recipeapp"
urlpatterns = [

    path('view',views.RecipeCreate.as_view(),name="view"),
    path('list',views.RecipeList.as_view(),name="recipe"),
    path('recipes/<int:pk>/',views.Detail.as_view(), name='recipe-detail'),
    path('review/<int:pk>/',views.Review.as_view(),name="review"),
    path('reviewcreate',views.ReviewCreate.as_view(),name="ReviewCreate"),
    path('search',views.Search.as_view(),name="search"),
    path('filter',views.RecipeFilter.as_view(),name="filter"),
]
