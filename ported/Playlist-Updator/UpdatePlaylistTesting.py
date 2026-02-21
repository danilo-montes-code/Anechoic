import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# def show_tracks(tracks):
#     for i, item in enumerate(tracks['items']):
#         track = item['track']
#         print("   %d %32.32s %s" % (i+1, track['artists'][0]['name'], track['name']))
#
#
# client_credentials_manager = SpotifyClientCredentials(client_id='id',
#                                                           client_secret='secret')
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# username = ''
# playlists = sp.user_playlists(username)
#
# for playlist in playlists['items']:
#         # if you own the playlist
#         if playlist['owner']['id'] == username and playlist['name'] == 'PUT PLAYLIST NAME HERE':
#             print()
#             print(playlist['name'])
#             print('  total tracks', playlist['tracks']['total'])
#             results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
#             tracks = results['tracks']
#             show_tracks(tracks)
#             while tracks['next']:
#                 tracks = sp.next(tracks)
#                 show_tracks(tracks)
#         else:
#             print("Can't pull data from", playlist['name'])

import spotipy.util as util
# SETX [/S system [/U [domain\]user [/P [password]]]] var value [/M]
# setx C://Rubikscrafter SPOTIPY_CLIENT_ID='id'

# SPOTIPY_CLIENT_ID='id'
# SPOTIPY_CLIENT_SECRET='secret'
# SPOTIPY_REDIRECT_URI='http://localhost:8888/'

username = ''
playlist_id = ''
track_ids = ['2ye824NM1m7Nc2UPXtwZjL', '6QPKYGnAW9QozVz2dSWqRg']

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("Can't get token for", username)
