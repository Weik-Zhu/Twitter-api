import json

f= open('da.txt','r')
tweets_data = []

for line in f:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

# for new york
knicks_count = 0
rangers_count = 0
nhl = []

for tweet in tweets_data:
    if 'stars' in tweet['text'].lower():
        nhl.append(tweet['text'])
        #print( tweet['created_at'] + '\t' + tweet['text'] + '\t' + str(tweet['user']['location']))
        knicks_count  = knicks_count + 1    
    elif 'mavericks' in tweet['text'].lower():
        #print(tweet['text'])
    	#print( tweet['created_at'] + '\t' + tweet['text'] + '\t' + str(tweet['user']['location']))
    	rangers_count = rangers_count + 1

print(len(tweets_data))
print('basketball are' + '\t' + str(knicks_count))
print('nfl are' + '\t' + str(rangers_count))
print(tweets_data[0]['created_at'])
print(tweets_data[17550]['created_at'])

