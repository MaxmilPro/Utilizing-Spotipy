import spotipy
import spotipy.util as util

#variables
username_1 = ''
username_2 = ''
client_id = ''
client_secret = ''
redirect_uri = 'http://:8888/callback'
dict_playlists = {}
dict_tracks = {}

#authorize user access and get access token for first user
token = util.prompt_for_user_token(username_1, client_id = client_id, client_secret = client_secret, redirect_uri = redirect_uri)
sp = spotipy.Spotify(auth=token)

#create dict of playlist names and Spotify playlist_ids
playlists = sp.user_playlists(username_1)
for item in playlists['items']:
    name = item['name']
    playlist_id = item['id']
    dict_playlists[name]=playlist_id

#create dict of playlist names (keys) and list of track ids (values)
for item in dict_playlists:
    try:
        tracks = sp.user_playlist_tracks(username_1, playlist_id = dict_playlists[item])
    except:
        continue
    lst = []
    for track in tracks['items']:
        lst.append(track['track']['id'])
    dict_tracks[item]=lst

#authorize user access and get access token for second user
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username_2, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)

#create playlists and add tracks
for item in dict_tracks:
    new_playlist = sp.user_playlist_create('maxmilpro', item)
    playlist_id = new_playlist['id']
    sp.user_playlist_add_tracks('maxmilpro', playlist_id, dict_tracks[item])





