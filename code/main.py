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
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="525dfddd96d94cb48637eeaf2bf98483",
                                                   client_secret="84f8cbd4c3714390b84bdfbaeb870596",
                                                   redirect_uri="http://localhost:3000",
                                                   scope=scope))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

"""
    How do we authenticate ourselves

    (1) Send a (POST/GET) request to get to the correct endpoint

    (2) Send out package (secrets CLIENTID/Secret)
    (3) Response is sent by SPOTIFY (failed/suceeded/error)
    (4) Read the response and if it is authenticated then we move on
"""
