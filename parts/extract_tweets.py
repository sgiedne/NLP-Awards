tweets_data_path = './goldenglobes.tab'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for tweet in tweets_file:
    try:
        tweets_data.append(tweet)
    except:
        continue