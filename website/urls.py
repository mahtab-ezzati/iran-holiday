from django.contrib import admin
from django.urls import path
from website.views import main_page

urlpatterns = [
    path('', main_page),

]