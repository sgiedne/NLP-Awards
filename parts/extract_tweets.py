import re

tweets_data_path = './goldenglobes.tab'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for tweet in tweets_file:
    try:
        tweets_data.append(tweet)
    except:
        continue
        
tweets_host_data = []

pattern = re.compile(".*host.*open.*")

for tweet in tweets_data:
    try:
        if pattern.match(tweet):
            tweets_host_data.append(tweet)
    except:
        continue

        
for i in tweets_host_data:
    print i
