"""
    Authors: Louis You & Jee Kim
    Purpose: Main file for the spotify project
"""
import secrets
import requests
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify
from spotipy.cache_handler import CacheFileHandler


def get_spotify_client() -> Spotify:
    """ Returns a spotipy client based on inside-function data. """
    spotify_client_id = ""
    spotify_client_secret = ""
    spotify_redirect_uri = "http://example.com"
    spotify_scope = "playlist-modify-private playlist-read-private"  # Allows us to read and modify private playlists
    spotify_cache_handler = CacheFileHandler("./token.txt")

    return Spotify(
        auth_manager=SpotifyOAuth(
            client_id=spotify_client_id,
            SECRET =spotify_client_secret,
            redirect_uri=spotify_redirect_uri,
            scope=spotify_scope,
            cache_handler=spotify_cache_handler
        )
    )

if __name__ == "__main__":
    print("Hello World!")

    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)


    # print(secrets.CLIENT_ID)


"""
    How do we authenticate ourselves

    (1) Send a (POST/GET) request to get to the correct endpoint
    (2) Send out package (secrets CLIENTID/Secret)
    (3) Response is sent by SPOTIFY (failed/suceeded/error)
    (4) Read the response and if it is authenticated then we move on
"""
