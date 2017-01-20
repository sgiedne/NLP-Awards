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
        
tweets_host_data = []

pattern = re.compile(".*host.*open.*")

for tweet in tweets_data:
    try:
        if pattern.match(tweet):
            tweets_host_data.append(tweet)
    except:
        continue
        
print '\nPotential tweets containing host name : \n--------------------\n'        
for i in tweets_host_data:
    print i
    
i=0
potential_hosts = []


for tweet in tweets_host_data:
    while(i < len(ne_chunk(pos_tag(word_tokenize(tweet))))):
        if(hasattr(ne_chunk(pos_tag(word_tokenize(tweet)))[i],'label')):
            if(ne_chunk(pos_tag(word_tokenize(tweet)))[i].label() == 'PERSON'):
                fname = ''.join(list(ne_chunk(pos_tag(word_tokenize(tweet)))[i][0][0]))
                lname = ''
                if(len(ne_chunk(pos_tag(word_tokenize(tweet)))[i]) > 1):
                    lname = ''.join(list(ne_chunk(pos_tag(word_tokenize(tweet)))[i][1][0]))
                potential_hosts.append(fname + ' ' + lname)
        i+=1;    
    i=0


print '\nPotential host names : '
print '\n--------------------\n'
for host in potential_hosts:
    print host
print '\n'
def most_common(lst):
 return max(set(lst), key=lst.count)

print '\nAnd the host is. . .\n***************************'
print most_common(potential_hosts)
print '***************************'