<img src="https://image.flaticon.com/icons/png/512/2111/2111685.png" width="70px">

## Spotify2py (under development Project)

# Installation

This library can be installed by the pip command, open your command prompt and type in the following command...

`pip install spotify2py`

# Overview of this library

First import the library using the **import** method `from spotify2py import Spotify` and then proceed to call the functions

### get_token()
- This function can be used to generate spotify api token.

- Use the function with Spotify **CLIENT_ID** & **CLIENT_SECRET** to generate a token.

```
from spotify2py import Spotify

var = Spotify().get_token(CLIENT_ID="your_CLIENT_ID", CLIENT_SECRET="your_CLIENT_SECRET")

print(var)
```

### recently_played()
- This function can be used list the recently played track names & track url.

- Use the function with **Spotify API Token**.

```
from spotify2py import Spotify

var = Spotify(token="token").recently_played(0)

print(var)
```

- Use the **show={}** method to check previous track.**(limit = 10)**

### External Links:
<a href="https://developer.spotify.com/documentation/web-api/">Spotify Web API documentation</a>
<br>
<a href="https://developer.spotify.com/dashboard/applications">Create a application</a>
<br>
<a href="https://developer.spotify.com/console/">Console</a>

