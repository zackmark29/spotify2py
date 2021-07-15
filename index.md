<img src="https://image.flaticon.com/icons/png/512/2111/2111685.png" width="70px" align="right">

# Spotify2py Docs

## Overview of this library

First import the library using the **import** method **from spotify2py import Spotify** and then proceed to call the functions

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

### user_profile()
- This function can be used to get meta data about user's profile .

- Use the function with **Spotify API Token** & **User ID.

```
from spotify2py import Spotify

var = Spotify(token="token", user_id="user-id").user_profile()

print(var)
```

<hr>

### user_playlists()
- This function can be used to get meta data about user's playlists.

- Use the function with **Spotify API Token** & **User ID.

```
from spotify2py import Spotify

var = Spotify(token="token", user_id="user-id").featured_playlist(show=0)

print(var)
```

- Use the **show={}** method to get previous or next playlist, **limit = based on user's playlists count**.

<hr>

### new_releases()
- This function can be used to get meta data about new releases albums.

- Use the function with **Spotify API Token**.

```
from spotify2py import Spotify

var = Spotify(token="token").new_releases(show=0)

print(var)
```

**Output of this program:**
```
{
    'album_name': 'Wasting Time ( feat. Drake )', 
    'album_url': 'https://open.spotify.com/album/2brWccDLT5vREu0FxqH6Az', 
    'album_image': 'https://i.scdn.co/image/ab67616d0000b2739b10373df0740a95838b7dd9'
}
```

- Use the **show={}** method to get previous or next playlist, **limit = 10**.

<hr>

### get_track()
- This function can be used to get meta data about track's.

- Use the function with **Spotify API Token** & **Track Name**.

```
from spotify2py import Spotify

var = Spotify(token="token").get_track("faded")

print(var)
```

**Output of this program:**
```
{
    'artist_name': 'Alan Walker', 
    'artist_url': 'https://open.spotify.com/artist/7vk5e3vY1uw9plTHJAMwjN', 
    'track_image': 'https://i.scdn.co/image/ab67616d0000b273c4d00cac55ae1b4598c9bc90', 
    'track_url': 'https://open.spotify.com/track/7gHs73wELdeycvS48JfIos', 
    'track_name': 'Faded', 
    'track_release_date': '2015-12-04'
}
```

<hr>

### play()
- This function can be used to play tracks on spotify web .

- Use the function with **Spotify API Token** & **Track Name**.

```
from spotify2py import Spotify

var = Spotify(token="token", user_id="user-id").play("alone marshmello")

print(var)
```
