import requests
import decouple
import json
import csv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from unidecode import unidecode

SPOTIFY_CLIENT_ID = decouple.config("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = decouple.config("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = decouple.config("SPOTIFY_REDIRECT_URI")
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1/"
ALL_SCOPES = "playlist-modify-private " \
             "playlist-read-private " \
             "playlist-modify-public " \
             "playlist-read-collaborative " \
             "user-read-private " \
             "user-read-email " \
             "ugc-image-upload " \
             "user-read-playback-state " \
             "user-modify-playback-state " \
             "user-read-currently-playing " \
             "user-library-modify " \
             "user-library-read " \
             "user-read-playback-position " \
             "user-read-recently-played " \
             "user-top-read " \
             "app-remote-control " \
             "streaming " \
             "user-follow-modify " \
             "user-follow-read"


def main():

    # playlist_name = input("Playlist name: ")
    # file_name = input("Name of the file with the list of songs: ")

    playlist_name = "Voyage a Paris"
    file_name = "voyage_a_paris.txt"

    # start spotify session
    sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                    client_id=SPOTIFY_CLIENT_ID,
                    client_secret=SPOTIFY_CLIENT_SECRET,
                    redirect_uri=SPOTIFY_REDIRECT_URI,
                    scope=ALL_SCOPES,
            )
    )

    song_list = get_song_list(file_name)
    song_list = parse_song_list(song_list)
    tracks_ids = search_songs(sp, song_list)

    # create playlist
    user = sp.current_user()
    user_id = user["id"]
    playlist_id = create_playlist(sp, user_id, playlist_name, save_info=True)

    # add tracks to playlist
    try:
        sp.playlist_add_items(playlist_id, tracks_ids)
    except requests.exceptions.HTTPError as e:
        raise e


def create_playlist(sp: spotipy.Spotify, user_id: str, name: str, save_info=False, indent=4) -> str:
    """creates new playlist and returns its id; if save_info=True, saves playlist info to file"""
    results = sp.user_playlist_create(user_id, name)

    if save_info:
        with open(f"{name}_playlist_data.json", mode="w", encoding="utf-8", newline="\n") as file:
            json.dump(results, file, indent=indent)

    return results["id"]


def search_songs(sp: spotipy.Spotify, song_list: list) -> list:
    """receives a spotipy session and a list of songs dicts and returns a list
    with ids for each track; saves not found songs in a file to search manually"""

    tracks_ids = []
    not_found = []

    for song in song_list:

        title = song["title"]
        artist = song["artist"]

        # search for each song
        try:
            results = sp.search(f"track:{title} artist:{artist}")
        except requests.exceptions.HTTPError as e:
            print(e)
            continue

        # get each track id
        try:
            track_id = results["tracks"]["items"][0]["id"]
            tracks_ids.append(track_id)

        # if it gets IndexError, it means that the search returned no results
        except IndexError:
            print(f"Not found: '{title}' by {artist}")
            not_found.append({"title": title, "artist": artist})

    # save not found tracks to search manually later
    with open("not_found(1).json", mode="w") as file:
            json.dump(not_found, file, indent=4)

    return tracks_ids


def get_song_list(file_name: str, csv_file=False) -> list:
    """gets song list from a txt file (or csv if csv_file=True)"""

    if csv_file:
        with open(f"{file_name}", newline="\n") as file:
            csvreader = csv.reader(file)
            contents = [row for row in csvreader]
    else:
        with open(f"{file_name}", encoding="utf-8") as file:
            contents = [line for line in file]

    return contents


def parse_song_list(song_list: list, sep="-") -> list:
    """gets rid of non ascii chars and other chars/words that may interfere with
    the search;
    returns a list with song dicts in the form {"title": title, "artist": artist}"""

    song_dicts = []
    for song in song_list:
        title_artist = song.split(sep=sep)
        title = title_artist[0]
        artist = title_artist[1]

        # parse title and artist strings to get more matches
        title = title.split("(")[0]
        title = title.split("/")[0]
        title = title.replace("'", "")
        title = title.replace("’", "")
        title = unidecode(title)    # get rid of accentuation

        artist = artist.split("Featuring")[0]
        artist = artist.split("featuring")[0]
        artist = artist.split("Duet")[0]
        artist = artist.split("With")[0]
        artist = artist.split("duet")[0]
        artist = artist.split("with")[0]
        artist = artist.split("&")[0]
        artist = artist.split("\n")[0]
        artist = artist.split("(")[0]
        artist = artist.split("/")[0]
        artist = artist.replace("'", "")
        artist = artist.replace("’", "")
        artist = artist.replace("+", " ")
        artist = unidecode(artist)  # get rid of accentuation

        song_dicts.append({"title": title, "artist": artist})

    return song_dicts


# if __name__ == '__main__':
#     main()

# sp = spotipy.Spotify(
#             auth_manager=SpotifyOAuth(
#                     client_id=SPOTIFY_CLIENT_ID,
#                     client_secret=SPOTIFY_CLIENT_SECRET,
#                     redirect_uri=SPOTIFY_REDIRECT_URI,
#                     scope=ALL_SCOPES,
#             )
#     )
#
# print(search_songs(sp, parse_song_list(get_song_list("voyage_a_paris.txt"))))
