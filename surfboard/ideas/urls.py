from django.contrib import admin
from django.urls import include, path

app_name = 'ideas'
urlpatterns = [
    path('', include('ideas.urls')),
]
