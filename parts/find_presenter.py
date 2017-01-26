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
        
print '\nTweets containing a presenter : \n--------------------\n' 
num_tweets = 0

for i in tweets_presenter_data:
    num_tweets += 1
    print i

print num_tweets



#Extract tweets that might have the presenter in it
#This doesn't quite work - it also captures things that are not people, and also takes a long time to load
'''
i=0
potential_presenters = []


for tweet in tweets_presenter_data:
    while(i < len(ne_chunk(pos_tag(word_tokenize(tweet))))):
        if(hasattr(ne_chunk(pos_tag(word_tokenize(tweet)))[i],'label')):
            if(ne_chunk(pos_tag(word_tokenize(tweet)))[i].label() == 'PERSON'):
                fname = ''.join(list(ne_chunk(pos_tag(word_tokenize(tweet)))[i][0][0]))
                lname = ''
                if(len(ne_chunk(pos_tag(word_tokenize(tweet)))[i]) > 1):
                    lname = ''.join(list(ne_chunk(pos_tag(word_tokenize(tweet)))[i][1][0]))
                potential_presenters.append(fname + ' ' + lname)
        i+=1;    
    i=0


print '\nPotential presenter names : '
print '\n--------------------\n'
for presenter in potential_presenters:
    print presenter
print '\n'
def most_common(lst):
 return max(set(lst), key=lst.count)

print '\nAnd the presenter is. . .\n***************************'
print most_common(potential_presenters)
print '***************************'
'''
