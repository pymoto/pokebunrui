from django.contrib import admin
from django.urls import path
from .views import randombtnfunc, indexfunc

urlpatterns = [
    path("randombtn/", randombtnfunc, name='randombtn'),
    path("", indexfunc, name='index')
]
