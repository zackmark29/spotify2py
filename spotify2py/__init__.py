from requests import get
from requests import post

class Spotify():
    def __init__(self, token):
        """
        Create a Application here: https://developer.spotify.com/dashboard/
        """
        self.token = token

    def recently_played(self, show=0):
        """Keywords : [spotify , name]"""

        json_response = get("https://api.spotify.com/v1/me/player/recently-played", headers={"Content-Type":"application/json", "Authorization":f"Bearer {self.token}"}).json()
        source =json_response['items'][show]["track"] 
        return dict(song = source['name'], album_url = source['external_urls']['spotify']) 

    def get_artist(self, artist_name):
        json_response = get(f"https://api.spotify.com/v1/search?query={artist_name}&type=artist&market=us&limit=1&offset=0", headers={"Content-Type":"application/json", "Authorization":f"Bearer {self.token}"}).json()
        source =json_response['artists']['items'][0]
        return dict(artist_name = source['name'], artist_url = source['external_urls']['spotify'], artist_image = source['images'][0]['url'], artist_total_followers = source['followers']['total'], artist_genres = source['genres'][0])    
        
    def get_token(self, CLIENT_ID, CLIENT_SECRET):
        return post("https://accounts.spotify.com/api/token", {'grant_type': 'client_credentials','client_id': CLIENT_ID,'client_secret': CLIENT_SECRET,}).json()['access_token']

    def get_album(self, album_name):
        json_response = get(f"https://api.spotify.com/v1/search?query={album_name}&type=album&market=us&limit=1&offset=0", headers={"Content-Type":"application/json", "Authorization":f"Bearer {self.token}"}).json()
        source =json_response['albums']['items'][0]
        return dict(artist_name = source['name'], album_url = source['external_urls']['spotify'], album_image = source['images'][0]['url'])    

