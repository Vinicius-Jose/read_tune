from django.test import TestCase
from parameterized import parameterized

from read_tune.services import ReadTuneAPI


class ReadTuneAPITest(TestCase):

    def setUp(self) -> None:
        self.api = ReadTuneAPI()
        return super().setUp()

    def test_authenticate(self) -> None:
        response = self.api.authenticate()
        assert response.get("Authorization")

    def test_get_generated_playlists(self) -> None:
        response: list[dict] = self.api.get_generated_playlists()
        assert response
        assert len(response) > 0
        assert response[0].get("id")
        assert response[0].get("link")

    def test_get_playlist_styles(self) -> None:
        response: list[dict] = self.api.get_playlist_styles()
        assert response
        assert len(response) > 1
        assert tuple(response[0].keys()) == ("name", "description")

    @parameterized.expand(
        [
            ("Men like gods", 5),
            ("Dracula", 5),
            ("The End of Eternity", 5),
        ],
    )
    def test_search_books(self, query: str, max_results: int) -> None:
        response: list[dict] = self.api.search_books(query, max_results)
        assert response
        assert len(response) <= max_results
        book = response[0]
        assert query.lower() in book.get("title").lower()

    def test_generate_playlist(self) -> None:
        query = "Dracula"
        max_results = 3
        response: list[dict] = self.api.get_playlist_styles()
        style: dict = response[0]
        assert style.get("name") == "Any Style"
        response: list[dict] = self.api.search_books(query, max_results)
        assert response
        assert len(response) <= max_results
        book: dict = response[0]
        assert query.lower() in book.get("title").lower()
        response: dict = self.api.generate_playlist(
            book.get("volume_id"), style.get("name"), max_songs=10, min_songs=3
        )
        assert response
        assert response.get("link")
        assert response.get("id")
