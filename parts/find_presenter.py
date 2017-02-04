import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords
import numpy

tweets_data_path = './goldenglobes.tab'
first_names_path = './names.txt'

stop_words = set(stopwords.words('english'))


first_names = []
first_names_file = open(first_names_path,"r")
for name in first_names_file:
    try:
        first_names.append(re.split('\n',name)[0])
    except:
        continue
        

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
presenter_award_result = []
i=0


split_tweet = re.split(' present.* Best ', tweet)

occurring_names = set()

count = 0

for tweet in tweets_presenter_data:
    split_tweet = re.split(' present.* Best ', tweet)
    
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
 
    split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
       
    presenter = []
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    if (chunk[0][0] + ' ' + chunk[1][0]) in occurring_names or chunk[0][0] not in first_names:
                        continue
                    presenter.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    presenter.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
    
    if len(presenter) > 0:
        filtered_split_right = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
    
        if len(filtered_split_right) > 0:
            print ' '.join(presenter) + ' presents award for Best ' + ' '.join(filtered_split_right)
            count +=1
            #print '  ---  presents award for Best ' 
            #print ' '.join(filtered_split_right)
            print '\n----------------\n'

print count
'''
#Extracts poeple(potential presenters) and organizations/GPEs(potential award names) within every tweet present in tweets_presenter_data. Resulting list in stored in presenter_award_data.
for tweet in tweets_presenter_data:
    chunked_data = ne_chunk(pos_tag(word_tokenize(tweet)))
    i=0
    #print ''
    n1 = []
    while(i<len(chunked_data)):
        if hasattr(chunked_data[i],'label'):
            
            #if chunked_data[i].label() == 'PERSON':
            if len(chunked_data[i]) > 1:
                n1.append(chunked_data[i][0][0] + ' ' + chunked_data[i][1][0])
            else:
                n1.append(chunked_data[i][0][0])
        i+=1
    presenter_award_data.append(n1)
    chunked_data = []
    

for i in presenter_award_data:
    print i
    print ''
'''