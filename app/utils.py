from .forms import *

import soundcloud
import os

client = soundcloud.Client(client_id = os.environ['client_id'],
                           client_secret = os.environ['client_secret'],
                           username = os.environ['username'],
                           password = os.environ['password']
                           )

def upload(track,name):
    track = client.post('/tracks',track={
         'title':name,
         'asset_data': track   #open(track,'rb')
         })


def resolve_url(track_url):    
    # resolve track URL into track resource
    track = client.get('/resolve', url=track_url)
    return track.id


def play(track_url):
    track_id=resolve_url(track_url)
    return track_id

def flw(user_url):
    user_id = resolve_url(user_url)
    client.put('/me/followings/%d' % user_id) 
    print "Followed"

