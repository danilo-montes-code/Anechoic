"""AnechoicCore.py

The class that contains the core functionality of the Anechoic application. 
"""
from __future__ import annotations

import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass



class AnechoicCore:
    def __init__(self):
        
        credentials = SpotifyClientCredentials(
            client_id=os.get_env("SPOTIPY_CLIENT_ID"), 
            client_secret=os.get_env("SPOTIPY_CLIENT_SECRET")
        )
        self.spotify = spotipy.Spotify(client_credentials_manager=credentials)


    def run(self):
        print("Running Anechoic Core...")