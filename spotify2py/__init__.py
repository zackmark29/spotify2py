from requests import get, post
from socket import gethostbyname, gethostname
from base64 import b64encode
import webbrowser as spotifyweb

class Spotify():
    def __init__(self, token=None, user_id=None):
        """
        Spotify2py
        ~~~~~~~~~~
        Create a Application: https://developer.spotify.com/dashboard/
        """
        self.token = token
        self.user_id = user_id

    def recently_played(self, show=0):
        try:
            json_response = get(f"https://api.spotify.com/v1/me/player/recently-played", 
            headers={
                "Content-Type":"application/json", 
                "Authorization":f"Bearer {self.token}"
                }
            ).json()
            
            source =json_response['items'][show]["track"]
            
            return dict(
                song = source['name'], 
                album_url = source['external_urls']['spotify']
            )

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def get_artist(self, artist_name):
        try:
            json_response = get(f"https://api.spotify.com/v1/search?query={artist_name}&type=artist&market=us&limit=1&offset=0", 
            headers={
                "Content-Type":"application/json", 
                "Authorization":f"Bearer {self.token}"
                }
            ).json()
            
            source = json_response['artists']['items'][0] 

            return dict(
                artist_name = source['name'], 
                artist_url = source['external_urls']['spotify'], 
                artist_image = source['images'][0]['url'], 
                artist_total_followers = source['followers']['total'], 
                artist_genres = source['genres'][0]
            )    

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def get_token(self, CLIENT_ID, CLIENT_SECRET):
        try:
            data = {
                'grant_type': 'client_credentials'
            }
            header = {
                'Authorization' : 'Basic {}'.format(b64encode(str(f"{CLIENT_ID}:{CLIENT_SECRET}").encode()).decode())
            }
            source = post("https://accounts.spotify.com/api/token", data=data, headers=header).json()
            return source['access_token']

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def get_album(self, album_name):
        try:
            json_response = get(f"https://api.spotify.com/v1/search?query={album_name}&type=album&market=us&limit=1&offset=0", 
            headers={
                "Content-Type":"application/json", 
                "Authorization":f"Bearer {self.token}"
                }
            ).json()

            source = json_response['albums']['items'][0]

            return dict(
                album_name = source['artists'][0]['name'], 
                album_url = source['external_urls']['spotify'], 
                total_tracks = source['total_tracks'],
                album_image = source['images'][0]['url'],
                artist_name = source['name'],
                album_release_date = source['release_date'],
                artist_url = source['artists'][0]['external_urls']['spotify']
            )    

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def featured_playlist(self, show=0):
        try:
            json_response = get("https://api.spotify.com/v1/browse/featured-playlists", 
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.token}"
                }
            ).json()
            
            source = json_response['playlists']['items'][show]

            return dict(
                playlist_name = source['name'],
                playlist_description = source['description'], 
                playlist_url = source['external_urls']['spotify'], 
                playlist_image = source['images'][0]['url']
            )    

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def new_releases(self, show=0):
        try:
            json_response = get("https://api.spotify.com/v1/browse/new-releases", 
            headers={
                "Content-Type":"application/json", 
                "Authorization":f"Bearer {self.token}"
                }
            ).json()

            source = json_response['albums']['items'][show]

            return dict(
                album_name = source['name'], 
                album_url = source['external_urls']['spotify'], 
                album_image = source['images'][0]['url']
            )    

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def user_playlists(self, show=0):
        try:
            json_response = get(f"https://api.spotify.com/v1/users/{self.user_id}/playlists", 
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.token}"
                }
            ).json()
            
            source = json_response['items'][show]

            return dict(
                playlist_name = source['name'],
                playlist_description = source['description'], 
                playlist_url = source['external_urls']['spotify'], 
                playlist_image = source['images'][0]['url'],
                playlist_owner = source['owner']['display_name']
            )    

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def user_profile(self):
        try:
            json_response = get(f"https://api.spotify.com/v1/users/{self.user_id}", 
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.token}"
                }
            ).json()
            
            source = json_response

            return dict(
                user_name = source['display_name'],
                user_followers = source['followers']['total'], 
                user_profile_url = source['external_urls']['spotify'], 
                playlist_image = source['images'][0]['url'],
            )    

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def markets(self):
        try:
            json_response = get("https://api.spotify.com/v1/markets", 
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.token}"
                }
            ).json()
            
            return json_response['markets']

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def get_track(self, track_name):
        try:
            json_response = get(f"https://api.spotify.com/v1/search?query={track_name}&type=track&limit=1", 
            headers={
                "Content-Type":"application/json", 
                "Authorization":f"Bearer {self.token}"
                }
            ).json()

            source = json_response['tracks']['items'][0]

            return dict(
                artist_name = source['album']['artists'][0]['name'], 
                artist_url = source['album']['artists'][0]['external_urls']['spotify'],
                track_image = source['album']['images'][0]['url'],
                track_url = source['external_urls']['spotify'], 
                track_name = source['album']['name'],
                track_release_date = source['album']['release_date'],
            )    
        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def play(self, track_name):
        try:
            json_response = get(f"https://api.spotify.com/v1/search?query={track_name}&type=track&limit=1", 
            headers={
                "Content-Type":"application/json", 
                "Authorization":f"Bearer {self.token}"
                }
            ).json()['tracks']['items'][0]['external_urls']['spotify']

            spotifyweb.open(json_response)

        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
