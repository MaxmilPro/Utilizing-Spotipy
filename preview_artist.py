import spotipy
import os,sys,time
import requests
from bs4 import BeautifulSoup
import shutil
spotify = spotipy.Spotify()
def ds(url,name):
	full = name + "-preview.mp3"
	response = requests.get(url, stream=True)
	with open(full,'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response	
def di(url, name):
	full = name + "_AlbumArt.jpg"
	response = requests.get(url, stream=True)
	with open(full,'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response	

artist_name = raw_input('Input Artist Name- \n')
artist_result = spotify.search(artist_name,limit=1,type='artist')
artist_id = 'spotify:artist:'+artist_result['artists']['items'][0]['id']
top_tracks = spotify.artist_top_tracks(artist_id)
os.mkdir(artist_name)
os.chdir(artist_name)
for track in top_tracks['tracks'][:10]:
	try:
		name = track['name']
		print "Downloading "+ name
		url = track['preview_url']
		ds(url,name)
	except:
		print "Couldn't download "+track['name']+" :( "
		continue
		
os.chdir('..')