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
        
'''        
print '\nPotential tweets containing host name : \n--------------------\n'        
for i in tweets_host_data:
    print i
'''   

i=0
potential_hosts = []
chunked_data = []


for tweet in tweets_host_data:
    chunked_data = ne_chunk(pos_tag(word_tokenize(tweet)))
    while(i < len(chunked_data)):
        if(hasattr(chunked_data[i],'label')):
            if(chunked_data[i].label() == 'PERSON'):
                fname = ''.join(list(chunked_data[i][0][0]))
                lname = ''
                if(len(chunked_data[i]) > 1):
                    lname = ''.join(list(chunked_data[i][1][0]))
                potential_hosts.append(fname + ' ' + lname)
        i+=1;    
    i=0
    chunked_data = []


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