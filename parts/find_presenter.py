import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import numpy

tweets_data_path = './goldenglobes.tab'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for tweet in tweets_file:
    try:
        tweets_data.append(tweet)
    except:
        continue
        
tweets_presenter_data = []

ceremony_name = "globes"

pattern = re.compile("(.* present.* Best.*)")
exclude_pattern = re.compile(".*(cli(p|ps)|nomin).*")

for tweet in tweets_data:
    try:
        if exclude_pattern.match(tweet):
            continue
        if pattern.match(tweet):
            tweets_presenter_data.append(tweet)
    except:
        continue
        
chunked_data = []
presenter_award_data = []
i=0

potential_presenters = []
#This looks at each tweet (document) in the tweets_presenter_data (corpus)
for tweet in tweets_presenter_data:
    try: 
        #Splits the tweet right before it mentions presenting/presents/presented the award 
        split_tweet = re.split(' present.* Best ', tweet)
        
        #With the split tweet, look only at the first split
        #Look from the end of the first split. If we hit a name, take that as the name
        #First, we need to tokenize each word
        tagged_words = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
        
        #Start from the end of the first split
        i = len(tagged_words) - 1

        print tweet
        while i >= 0:
            if hasattr(tagged_words[i], 'label'):
                #Do not consider any "GoldenGlobes"
                if "Golden" not in str(tagged_words[i]):
                    #potential_presenters.append(list(tagged_words[i])) (ADD THIS LATER)
                    #Print anything in the first split that has a label that is not GoldenGlobes
                    #PROBLEM: Misses anything with "@" in front of it
                    #PROBLEM: How to deal with retweet RT "@"s?
                    print tagged_words[i]
            i=i-1

        #ALTERNATIVE 1: We could calculate TFIDF and take the name as the one with the highest TFIDF
        #ALTERNATIVE 2: We could also look for "and" in tagged_words and see if there are pronouns around them 
        
        #NEXT: Now look at the second split and see if you can find the presenter there 
        #This will help us determine when the presenter might be mentioned in the second half of the tweet
    except:
        continue

#Testing structure of tweets with "Golden Globes" before " present"
split_tweet1 = re.split(' present.* Best ', tweets_presenter_data[6])
print split_tweet1
#print potential_presenters
    