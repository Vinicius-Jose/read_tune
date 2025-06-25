from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from requests.exceptions import ConnectionError

from read_tune.services import ReadTuneAPI

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    api = ReadTuneAPI()
    playlists = []
    try:
        playlists = api.get_generated_playlists()
    except ConnectionError:
        pass
    return render(request, "read_tune/index.html", {"playlists": playlists})


def search_book(request: HttpRequest) -> HttpResponse:
    api = ReadTuneAPI()
    query = request.GET.get("query")
    books = api.search_books(query)
    styles = api.get_playlist_styles()
    return render(
        request, "read_tune/book_list.html", {"books": books, "styles": styles}
    )


def generate_playlist(request: HttpRequest, volume_id: str) -> HttpResponse:
    api = ReadTuneAPI()
    style = request.GET.get("style")
    max_songs = request.GET.get("max_songs", 10)
    min_songs = request.GET.get("min_songs", 10)
    playlist = api.generate_playlist(
        volume_id=volume_id,
        playlist_style=style,
        max_songs=max_songs,
        min_songs=min_songs,
    )
    return render(request, "read_tune/playlist_generated.html", {"playlist": playlist})
