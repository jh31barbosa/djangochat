from pathlib import Path
from sys import path_hooks, path_importer_cache
from django.urls import path

from . import views

urlpatterns = [
    path('',views.rooms, name='rooms'),
    path('<slug:slug>/',views.room, name='room'),
]
