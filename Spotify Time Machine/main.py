import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

API_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
API_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL, headers=header)

billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=API_CLIENT_ID,
        client_secret=API_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Denizhan"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for Songs by Title

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# Creating a private playlist in Spotify

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                                   public=False, description="Top 100 songs created with Spotipy API")

# Adding songs to the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
