import encoding_fix
import json
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, parser=tweepy.parsers.RawParser())

@classmethod                    
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

f= open('your_name.txt','w')
class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        f.write(json.dumps(tweet._json))
        f.write('\n')

    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth, listener=l)

keywords = ['rangers', 'knicks']
streamer.filter(track = keywords, locations = [-73.994553, 40.750140, -73.992767,40.751120])

# los angle
#streamer.filter(locations = [-118.26803,34.042572,-118.265755,34.043906],track = keywords)

# new york
#-73.994553, 40.750140, -73.992767,40.751120
