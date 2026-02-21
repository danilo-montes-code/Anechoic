# Updates a playlist in reference to other playlists
# Pulls data from other playlists and removes songs that are no longer in said playlists
# Basically a playlist merger
# https://spotipy.readthedocs.io/en/latest
# developer.spotify.com

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

# Makes sure that the answer to a posed question is an integer value, repeating the prompt if not
def make_sure_is_a_number(question):
    try:
        print()
        text = input(question).lower()
        num = int(text)
    except ValueError:
        print('Please enter a integer value.')
    else:
        return num


# adds the ids of the tracks in the given playlist to a list
def add_tracks_to_list(tracks, playlist):
    for item in tracks['items']:
        playlist.append(item['track']['id'])

    while tracks['next']:
        tracks = sp.next(tracks)
        add_tracks_to_list(tracks, playlist)
    return playlist


# Gets the main playlist
def get_main_playlist(playlists):
    main_playlist = 'monarchy'   # input('What is the name of the main playlist?: ').lower()
    for playlist in playlists['items']:
        # if you own the playlist and the name of the playlist is the playlist name given by the user, return playlist
        if playlist['owner']['id'] == username and playlist['name'].lower() == main_playlist:
            return playlist
    print('Playlist name does not match any of the public playlists that you own')
    get_main_playlist(playlists)


# Gets the playlists that songs are being pulled from
def get_sub_playlists(playlists):
    sub_playlist_amount = 2   # make_sure_is_a_number('How many playlists do you want to pull data from?: ')
    # while type(sub_playlist_amount) is not int:
    #     sub_playlist_amount = make_sure_is_a_number('How many playlists do you want to pull data from?: ')
    sub_playlist_names = ['monarch v', 'monarch vi']  # []
    # for i in range(0, sub_playlist_amount):
    #     sub_playlist_names.append(input(f'What is the name of playlist #{i+1}?: ').lower())

    sub_playlists = []
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            playlist_name_placeholder = playlist['name'].lower()
            for sub_playlist in sub_playlist_names:
                if sub_playlist == playlist_name_placeholder:
                    sub_playlists.append(playlist)
    return sub_playlists


# Gets the missing tracks
def get_tracks(main_playlist, sub_playlists):
    # gets the ids of the songs already in the main playlist
    main_playlist_tracks = []
    results = sp.user_playlist(username, main_playlist['id'], fields="tracks,next")
    tracks = results['tracks']
    main_playlist_tracks = add_tracks_to_list(tracks, main_playlist_tracks)

    # gets the ids of the songs in the sub playlists
    sub_playlist_tracks = []
    for playlist in sub_playlists:
        results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        sub_playlist_tracks = add_tracks_to_list(tracks, sub_playlist_tracks)

    # removes duplicate tracks from across the sub playlists
    sub_playlist_tracks = list(dict.fromkeys(sub_playlist_tracks))

    # returns a list of ids for the missing tracks
    return get_missing_tracks(main_playlist_tracks, sub_playlist_tracks)


# Returns the tracks missing from the main playlist that are present in the sub playlists
def get_missing_tracks(main_playlist_songs, sub_playlist_songs):
    missing_tracks = []
    if len(main_playlist_songs) != 0:
        for song in main_playlist_songs:
            for sub_song in sub_playlist_songs:
                if song != sub_song and not song_is_in_main_playlist(main_playlist_songs, sub_song):
                    missing_tracks.append(sub_song)  # Puts song in the missing songs list
                    main_playlist_songs.append(sub_song)  # Puts in it the main playlist list to not check again
        return missing_tracks
    else:
        return sub_playlist_songs


# returns true if the given song is in the main playlist already
def song_is_in_main_playlist(main_playlist_songs, song):
    in_list = False
    for track in main_playlist_songs:
        if track == song:
            in_list = True
            break
    return in_list


# Removes songs that are not in the sub playlists but is in the main playlist
def remove_songs():
    pass


def main():
    # gets the playlists from the user
    playlists = sp.user_playlists(username)

    # sets the main playlist
    main_playlist = get_main_playlist(playlists)

    # sets the sub playlists
    sub_playlists = get_sub_playlists(playlists)

    # list of the ids of the missing tracks
    tracks = get_tracks(main_playlist, sub_playlists)

    for track in tracks:
        print(track)

    # adds the missing tracks to the main playlist
    # scope = 'playlist-modify-public'
    # util.prompt_for_user_token(username, scope, 'id',
    #                            'secret', 'http://localhost:8888/')
    # sp.trace = False
    # results = sp.user_playlist_add_tracks(username, main_playlist['id'], tracks)
    # print(results)
    # sp.user_playlist_add_tracks(username, main_playlist['id'], tracks)


if __name__ == '__main__':
    # sets up the credentials for the spotipy object
    client_credentials_manager = SpotifyClientCredentials(client_id='',
                                                          client_secret='')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # the username of the user, taken from spotify uri
    username = ''
    main()
