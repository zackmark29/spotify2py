<img src="https://image.flaticon.com/icons/png/512/2111/2111685.png" width="70px">

Spotify Web API documentation : https://developer.spotify.com/documentation/web-api/

**use the Example code given below 👇,To get details about the artist.**

```py
from spotify2py import get_artist

source = get_artist(artist_name="marshmello", token="BQCQ.........g49Y9t3Y")

print(source)
```

<hr>

**The access tokens expire after 1 hour, which is set by Spotify's side and follows OAuth2 Guidelines.**

**But you can create a new token using CLIENT_ID & CLIENT_SECRET.**

**use the code given below 👇,To generate a new Token.**

```py
from spotify2py import get_token

CLIENT_ID = '17a3.......90c20660f8'
CLIENT_SECRET = '584d2ee.....07f8'

print(get_token(CLIENT_ID, CLIENT_SECRET))
```
