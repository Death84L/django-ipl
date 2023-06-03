"""
URL configuration for ipl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views
# task  1,2,5,
urlpatterns = [
    path('', views.house,name='house'),
    path('matches_per_year/', views.matches_per_year, name='matches_per_year'),
    path('matches_won_by_teams/', views.matches_won_by_teams, name='matches_won_by_teams'),
    path('matches_played_vs_won/', views.matches_played_vs_won, name='matches_played_vs_won'),
    path('admin/', admin.site.urls),
]
