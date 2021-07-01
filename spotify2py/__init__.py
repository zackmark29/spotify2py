from requests import get, post
from socket import gethostbyname, gethostname

class Spotify():
    def __init__(self, token):
        """
        Spotify2py
        ~~~~~~~~~~
        Create a Application: https://developer.spotify.com/dashboard/
        """
        self.token = token

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
        except KeyError:
            return f"401 Error : {json_response['error']['message']}"
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
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
        except KeyError:
            return f"401 Error : {json_response['error']['message']}"
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def get_token(self, CLIENT_ID, CLIENT_SECRET):
        try:
            json_response = post("https://accounts.spotify.com/api/token",
            {
                'grant_type': 'client_credentials',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            }
            ).json()

            return json_response['access_token']
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
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
                album_name = source['name'], 
                album_url = source['external_urls']['spotify'], 
                album_image = source['images'][0]['url']
            )    
        except KeyError:
            return f"401 Error : {json_response['error']['message']}"
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
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
        except KeyError:
            return f"401 Error : {json_response['error']['message']}"
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
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
        except KeyError:
            return f"401 Error : {json_response['error']['message']}"
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"

    def user_playlists(self, user_id, show=0):
        try:
            json_response = get(f"https://api.spotify.com/v1/users/{user_id}/playlists", 
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
        except KeyError:
            return f"401 Error : {json_response['error']['message']}"
        except TypeError as __error__:
            return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
        except Exception as __error__:
            if f"{gethostbyname(gethostname())}" == "127.0.0.1":
                return "You're Offline."
            else:
                return f"Please Report the issue to developer, 'Error : {__error__}' on 'https://github.com/sijey-praveen/spotify2py/issues'"
