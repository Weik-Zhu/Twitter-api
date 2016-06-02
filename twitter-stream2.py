import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
    	if 'lakers' in tweet.text:
            print(tweet.author.screen_name + "\t" + str(tweet.created_at) + "\t" + tweet.text)
        

    def on_error(self, status_code):
        print( 'Error: ' + repr(status_code))
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth, listener=l)

keywords = ['lakers']
streamer.filter(track = keywords)


streamer.filter(track = keywords, locations= [-118.26803,34.042572,-118.265755,34.043906])

