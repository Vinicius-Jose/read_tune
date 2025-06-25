import requests
import os


class ReadTuneAPI:

    def __init__(self) -> None:
        self.url = os.environ.get("READ_TUNE_API_URL")
        self.headers = {"Content-Type": "application/json"}

    def authenticate(self) -> dict:
        if self.headers.get("Authorization"):
            return self.headers.get("Authorization")
        email = os.environ.get("READ_TUNE_API_EMAIL")
        pwd = os.environ.get("READ_TUNE_API_PASSWORD")
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = f"grant_type=password&username={email}&password={pwd}"
        url = f"{self.url}/token"
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            response = response.json()
            auth = {
                "Authorization": f"{response['token_type']} {response['access_token']}"
            }
            self.headers.update(auth)
            return auth
        return {}

    def get_generated_playlists(self) -> list[dict]:
        self.authenticate()
        url = f"{self.url}/spotify/playlist"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else []

    def get_playlist_styles(self) -> list[dict]:
        self.authenticate()
        url = f"{self.url}/llm/style"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else []

    def search_books(self, query: str, max_results: int = 10) -> list[dict]:
        self.authenticate()
        url = f"{self.url}/books"
        params = {"query": query, "max_results": max_results}
        response = requests.get(url, params=params, headers=self.headers)
        return response.json() if response.status_code == 200 else []

    def generate_playlist(
        self, volume_id: str, playlist_style: str, max_songs: int, min_songs: int
    ) -> dict:
        self.authenticate()
        params = {
            "playlist_style": playlist_style,
            "min_songs": min_songs,
            "max_songs": max_songs,
        }
        url = f"{self.url}/llm/{volume_id}"
        response = requests.get(url, params=params, headers=self.headers)
        return response.json() if response.status_code == 200 else []
