"""
    Authors: Louis You & Jee Kim
    Purpose: Main file for the spotify project
"""
import secrets
import requests

# Easy way to work with Spotify API
import spotipy

# Class that bundles the credentials and sends it to JSON(?)
from spotipy.oauth2 import SpotifyOAuth


if __name__ == "__main__":
    print("Hello World!")
    scope = "user-library-read" # Url extender (defines what data what we get back from API) [3 recommendation for each song]
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.CLIENT_ID,
                                                   scope=scope, 
                                                   client_secret=secrets.CLIENT_SECRET,
                                                   redirect_uri=secrets.REDIRECT_URI))
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

"""

"""
