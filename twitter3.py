import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#public_tweets = api.search('lakers', geocode='36.8,-121.75,10mi',count=5)
public_tweets = api.search('@Forterranw', count=100)

for tweet in public_tweets:
    print(tweet.user.screen_name + "\t" + str(tweet.created_at) + "\t" + tweet.text[:100])

#for tweet in public_tweets:
#	if tweet.retweet_count != 0:
#		print(tweet.user.screen_name+ "\t" +str(tweet.created_at)+ 
#			"\t" +str(tweet.retweet_count)+ "\t" + tweet.text)

# get the url in each tweet
#for tweet in public_tweets:
#	print(tweet.entities['urls'][0]['url'])

#tweets = api.search('hi', geocode='47.654174,-122.303239,2mi', count= 5)