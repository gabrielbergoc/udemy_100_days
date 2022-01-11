import requests
import decouple
import csv
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
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

    date = input("Which date do you want to travel to? (YYYY-MM-DD): ")

    try:
        response = requests.get(BILLBOARD_URL + date)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        raise errh
    except requests.exceptions.ConnectionError as errc:
        raise errc
    except requests.exceptions.Timeout as errt:
        raise errt
    except requests.exceptions.RequestException as err:
        raise err

    soup = BeautifulSoup(response.text, "html.parser")

    billboard = [
        {
            "title": title.getText(),
            "rank": rank.getText(),
            "artist": artist.getText(),
        } for title, rank, artist in zip(
                soup.select(selector=".chart-element__information__song"),
                soup.select(selector=".chart-element__rank__number"),
                soup.select(selector=".chart-element__information__artist")
                )
    ]
    # save_billboard(billboard, date)

    sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                    client_id=SPOTIFY_CLIENT_ID,
                    client_secret=SPOTIFY_CLIENT_SECRET,
                    redirect_uri=SPOTIFY_REDIRECT_URI,
                    scope=ALL_SCOPES,
            )
    )

    user = sp.current_user()
    user_id = user["id"]

    # create playlist
    playlist_id = create_playlist(sp, user_id, f"{date} Billboard 100", save_info=True)

    tracks_ids = []
    not_found = []
    for song in billboard:

        # parse title and artist strings to get more matches
        title = song["title"].replace("'", "")
        title = title.replace("-", " ")
        title = title.split("(")[0]
        title = title.split("/")[0]
        artist = song["artist"].replace("'", "")
        artist = artist.replace("+", " ")
        artist = artist.split("Featuring")[0]
        artist = artist.split("featuring")[0]
        artist = artist.split("Duet")[0]
        artist = artist.split("With")[0]
        artist = artist.split("duet")[0]
        artist = artist.split("with")[0]
        artist = artist.split("&")[0]

        # search each song
        try:
            results = sp.search(f"track:{title} artist:{artist}")
            # save_track_query(title, artist, results)
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

    # add tracks to playlist
    try:
        sp.playlist_add_items(playlist_id, tracks_ids)
    except requests.exceptions.HTTPError as e:
        raise e

    # check to see if items were added+
    # print(sp.playlist_items(playlist_id))


def save_track_query(title, artist, data, indent=4):
    with open(f"{title}_{artist}_spotify_query.json", mode="w") as file:
        json.dump(data, file, indent=indent)

    print(f"data saved to {title}_{artist}_spotify_query.json")

def save_billboard(billboard, date, csv_file=True):
    """save billboard information to file; if csv=False, save to .txt in a legible format"""
    if csv_file:
        with open(f"billboard-{date}.csv", mode="w", encoding="utf-8", newline="\n") as file:
            csvwriter = csv.writer(file, quotechar="`")
            for song in billboard:
                csvwriter.writerow((song['rank'], song['title'], song['artist']))
    else:
        with open(f"billboard-{date}.txt", mode="w", encoding="utf-8", newline="\n") as file:
            for song in billboard:
                file.write(f"{song['rank']}) {song['title']} - {song['artist']}\n")

            # print(f"{song['rank']}) {song['title']} - {song['artist']}")

def create_playlist(sp: spotipy.Spotify, user_id: str, name: str, save_info=False, indent=4):
    """creates new playlist and returns its id; if save_info=True, saves playlist info to file"""
    results = sp.user_playlist_create(user_id, name)

    if save_info:
        with open(f"{name}_playlist_data.json", mode="w", encoding="utf-8", newline="\n") as file:
            json.dump(results, file, indent=indent)

    return results["id"]


if __name__ == '__main__':
    main()
