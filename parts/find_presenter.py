import re
import urllib2
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords
import numpy

tweets_data_path = './goldenglobes.tab'
first_names_path = './names.txt'

stop_words = set(stopwords.words('english'))


def getusername(handle):
    try:
        raw_data = urllib2.urlopen("https://twitter.com/search?q=%40" + handle).read()
        scripted_html = re.split(">",re.split('ProfileNameTruncated-link u-textInheritColor js-nav js-action-profile-name',raw_data)[1])
        untrimmed_name = re.split("<",scripted_html[1])
        trimmed_name = re.split("\n",untrimmed_name[0])
        return trimmed_name[1].strip()
    except:
        return handle


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
occurring_handles = set()
count = 0

print ''

for tweet in tweets_presenter_data:
    split_tweet = re.split(' present.* Best ', tweet)
    
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    

    split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
       
    presenter = []
    
    
    #For twitter handles
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
    
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        presenter.append(getusername(handle))
        occurring_handles.add(handle)
    
    
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
            print ' '.join(presenter) + ' presented the award for Best ' + ' '.join(filtered_split_right)
            count +=1
            #print '  ---  presents award for Best ' 
            #print ' '.join(filtered_split_right)
            print '\n----------------\n'