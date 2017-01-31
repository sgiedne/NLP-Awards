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

#Extracts poeple(potential presenters) and organizations/GPEs(potential award names) within every tweet present in tweets_presenter_data. Resulting list in stored in presenter_award_data.
for tweet in tweets_presenter_data:
    chunked_data = ne_chunk(pos_tag(word_tokenize(tweet)))
    i=0
    #print ''
    n1 = []
    
    while(i<len(chunked_data)):
        str_data = str(chunked_data[i])
        #Considers only the chunked data before the first mention of "Best"
        if "Best" not in str_data:
            #Detects variations of Golden Globes in the chunked data (DOESN'T QUITE WORK YET!)
            if (hasattr(chunked_data[i],'label') and not (("Golden" in str_data) or ("Globe" in str_data))):
                n1.append(str_data)
            i+=1
        else:
            break

        presenter_award_data.append(n1)
        chunked_data = []

for i in presenter_award_data:
    print i
    print ''
