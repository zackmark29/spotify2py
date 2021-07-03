<img src="https://image.flaticon.com/icons/png/512/2111/2111685.png" width="70px" align="right">

# Spotify2py

## Installation

This library can be installed by the pip command, open your command prompt and type in the following command...

`pip install spotify2py`

## Overview of this library

First import the library using the **import** method `from spotify2py import Spotify` and then proceed to call the functions

### get_token()
- This function can be used to generate spotify api token.

- Use the function with Spotify **CLIENT_ID** & **CLIENT_SECRET** to generate a token.

```
from spotify2py import Spotify

var = Spotify().get_token(CLIENT_ID="your_CLIENT_ID", CLIENT_SECRET="your_CLIENT_SECRET")

print(var)
```

<hr>

### recently_played()
- This function can be used list the recently played track names & track url.

- Use the function with **Spotify API Token**.

```
from spotify2py import Spotify

var = Spotify(token="token").recently_played(show=0)

print(var)
```

- Use the **show={}** method to get previous track, **limit = 10**.

<hr>

### get_artist()
- This function can be used to get meta data about artists.

- Use the function with **Spotify API Token** & **Artist Name**.

```
from spotify2py import Spotify

var = Spotify(token="token").get_artist("alan walker")

print(var)
```

**Output of this program:**
```
{
    'artist_name': 'Alan Walker', 
    'artist_url': 'https://open.spotify.com/artist/7vk5e3vY1uw9plTHJAMwjN', 
    'artist_image': 'https://i.scdn.co/image/ab6761610000e5ebfc16b9995c5301d3f7e5fad4', 
    'artist_total_followers': 29131930, 
    'artist_genres': 'electro house'
}
```

<hr>

### get_album()
- This function can be used to get meta data about album.

- Use the function with **Spotify API Token** & **Album Name**.

```
from spotify2py import Spotify

var = Spotify(token="token").get_album("shockwave")

print(var)
```

**Output of this program:**
```
{
    'album_name': 'Marshmello', 
    'album_url': 'https://open.spotify.com/album/6yXPyhVxt3PHBwkinPFn6I', 
    'total_tracks': 12, 
    'album_image': 'https://i.scdn.co/image/ab67616d0000b273d82de295af2bbdc06fb14068', 
    'artist_name': 'Shockwave', 
    'album_release_date': '2021-06-11', 
    'artist_url': 'https://open.spotify.com/artist/64KEffDW9EtZ1y2vBYgq8T'
}
```

<hr>

### featured_playlist()
- This function can be used to get meta data about featured playlist of your spotify account.

- Use the function with **Spotify API Token**.

```
from spotify2py import Spotify

var = Spotify(token="token").featured_playlist(show=0)

print(var)
```

**Output of this program:**
```
{
    'playlist_name': 'Easy On Saturday', 
    'playlist_description': 'Lekker rustig aan doen op zaterdag met deze zachte pop liedjes.', 
    'playlist_url': 'https://open.spotify.com/playlist/37i9dQZF1DX79N7YUDFu8f', 
    'playlist_image': 'https://i.scdn.co/image/ab67706f00000003e62a57481e6aaeb533bea9b3'
}
```

- Use the **show={}** method to get previous or next playlist, **limit = 10**.

<hr>

## External Links:
<a href="https://developer.spotify.com/documentation/web-api/">Spotify Web API documentation</a>
<br>
<a href="https://developer.spotify.com/dashboard/applications">Create a application</a>
<br>
<a href="https://developer.spotify.com/console/">Spotify Web API Console</a>

