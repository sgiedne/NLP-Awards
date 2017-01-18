import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

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

print "untokenized tweets"
for i in tweets_host_data:
    print i

tweet1 = tweets_host_data[0]

def tag_tweet(tweet):
    tokenized = nltk.word_tokenize(tweet)
    tagged = nltk.pos_tag(tokenized)
    print tagged

tag_tweet(tweet1)