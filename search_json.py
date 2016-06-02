import encoding_fix
import tweepy
import json
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
keywords = ['houston rockets','houston texans']
tweets = api.search(keywords, count = 1000)

fh= open('sample_tweet.txt','w')

for tweet in tweets:
    fh.write(json.dumps(tweet._json, sort_keys = True)) 
    fh.write('\n')
    
fh = open('sample_tweet.txt','r')

for line in fh:
    tweet = json.loads(line)
    print(tweet['user'])
    

#tweets = api.search('hi', geocode='47.654174,-122.303239,2mi', count= 5)
#print(tweet['possibly_sensitive'])

