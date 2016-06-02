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

f= open('da1.txt','w')
class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        f.write(json.dumps(tweet._json))
        f.write('\n')

    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth, listener=l)

#keywords = ['rangers', 'knicks']
#streamer.filter(track = keywords, locations = [-73.994553, 40.750140, -73.992767,40.751120])

# los angle
#keywords = ['lakers', 'kings']
#streamer.filter(locations = [-118.26803,34.042572,-118.265755,34.043906],track = keywords)

# new york
#keywords = ['rangers', 'knicks']
#streamer.filter(track = keywords, locations = [-73.994553, 40.750140, -73.992767,40.751120])

# chicago get
#keywords = ['blackhawks', 'bulls']
#streamer.filter(track = keywords, locations = [-87.675342,41.880097, -87.673189,41.881348])

# washington
#keywords = ['capitals', 'wizards']
#streamer.filter(track = keywords, locations = [-77.021831,38.897474, -77.020071,38.898643])

# philadelphia 5/25 from 9.30 to 1.11
#keywords = ['flyers', '76ers']
#streamer.filter(track = keywords, locations = [-75.173096,39.900578, -75.170854,39.901837])
#
# dallas  get
keywords = ['dallas stars', 'dallas mavericks']
streamer.filter(track = keywords, locations = [-96.811189,32.789630, -96.809730,32.791235])

# toronto
#keywords = ['maple leafs', 'raptors']
#streamer.filter(track = keywords, locations = [-79.380104,43.642678, -79.378302,43.644177])
