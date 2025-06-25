from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book", views.search_book, name="book"),
    path("book/<str:volume_id>/", views.generate_playlist, name="generate_playlist"),
]
