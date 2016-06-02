import json
import pandas as pd
from state import *
import copy

data1 = open('dallas.txt','r')
keyword = ['mavericks','stars']

# read json into list
tweets_data = []

for line in data1:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue    
# classify data into nba and nhl
nba_fans_location = []
nhl_fans_location = []

nba_fans_des = []
nhl_fans_des = []
test = []
for tweet in tweets_data:
    if keyword[0] in tweet['text'].lower():
        
        nba_fans_location.append(tweet['user']['location'])
        nba_fans_des.append(tweet['user']['description'])
    elif keyword[1] in tweet['text'].lower():
        test.append(tweet['text'].lower())
        nhl_fans_location.append(tweet['user']['location'])  
        nhl_fans_des.append(tweet['user']['description'])

# calcualte real fans
nba_real_fans = 0
nhl_real_fans = 0

for des in nba_fans_des:
    if des != None:
        if keyword[0] in des.lower():
            nba_real_fans += 1
            
for des in nhl_fans_des:
    if des != None:
        if keyword[1] in des.lower():
            nhl_real_fans += 1

print('NBA')
print(len(nba_fans_des))
print(nba_real_fans)
print(nba_real_fans*100/len(nba_fans_des))
print('NHL')
print(len(nhl_fans_des))
print(nhl_real_fans)
print(nhl_real_fans*100/len(nhl_fans_des))
# get distribution of location of fans
nba_location_count = copy.copy(states)
nhl_location_count = copy.copy(states)

for location in nba_fans_location:
    if location != None:
        temp = location.split(',')[-1].strip().upper()
        if temp in states.keys():
            nba_location_count[temp] += 1
        
for location in nhl_fans_location:
    if location != None:
        temp = location.split(',')[-1].strip().upper()
        if temp in states.keys():
            nhl_location_count[temp] += 1   
# build dataFrame and save it
tweets = pd.DataFrame()
tweets['NBA'] = nba_location_count.values()
tweets['NHL'] = nhl_location_count.values()
tweets['total'] = tweets.NBA + tweets.NHL
tweets.index = states.keys()
tweets.to_excel('dallas.xls')