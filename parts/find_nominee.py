from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.stem import PorterStemmer
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import unicodedata
import re
import numpy
import string
import nltk

kwdA1="actor"
kwdA2="actress"

kwdB1="motion"
kwdB2="picture"
kwdB3="supporting"
kwdB4="role"
kwdB5="television"
kwdB6="series"
kwdB7="limited"
kwdB8="series"

kwdC1="drama"
kwdC2="musical"
kwdC3="or"
kwdC4="comedy"
kwdC5="motion"
kwdC6="picture"
kwdC7="Television"
kwdC8="television"
kwdC9="television"
kwdC10="Tv"
kwdC11="tv"
kwdC12="movie"

kwdD1="best"
kwdD2="performance"
kwdD3="director"
kwdD4="screenplay"
kwdD5="animated"
kwdD6="foreign"
kwdD7="language"
kwdD8="original"
kwdD9="score"
kwdD10="song"

kwdE1="donald"
kwdE2="trump"
kwdE3="powerful"
kwdE4="speech"

kwdList=[kwdA1,kwdA2,kwdB1,kwdB2,kwdB3,kwdB4,kwdB5,kwdB6,kwdB7,kwdB8,kwdC1,kwdC2,kwdC3,kwdC4,kwdC5,kwdC6,kwdC7,kwdC8,kwdC9,kwdC10,kwdC11,kwdC12,kwdD1,kwdD2,kwdD3,kwdD4,kwdD5,kwdD6,kwdD7,kwdD8,kwdD9,kwdD10,kwdE1,kwdE2,kwdE3,kwdE4]

def mergeDicts(dict1, dict2):
    A = Counter(dict1)
    B = Counter(dict2)
    C=A+B
    return C

    
def trackNameBackinFullTweets(potentialWinner,potentialList):
   relatedTweetsCount=0
   nameDic = {}
   for tweet in potentialList:
     if potentialWinner.title() in tweet:
        key=checkPairedName(potentialWinner, tweet)       
        if key in nameDic:
            nameDic[key]=nameDic[key]+1
        else:
            nameDic[key]=0


def getPotentialWinner(nameDic):
    if not nameDic:
        #print ("No result find")
        return ''
    else:
        result = max(nameDic, key=lambda key: nameDic[key])
        return result
        #print("The winner is "+str(result))
    
    

def trackNameBackinTweet(potentialWinner,potentialList):
  
   
   nameDic = {}
   for tweet in potentialList:
     if potentialWinner in tweet:
        key=checkPairedName(potentialWinner, tweet)
        if key!=None:
          if key in nameDic:
             nameDic[key]=nameDic[key]+1
          else:
             nameDic[key]=1
   #print(len(nameDic))
   if len(nameDic)==0:
      print ("")
      #trackNameBackinFullTweets(potentialWinner,tweets_data)
   else:
    
      
       #print (nameDic)
       return nameDic
      #getPotentialWinner(nameDic)
     
    


def checkPairedName(potentialWinner,tweet):
   text = word_tokenize(tweet)
   rst=nltk.pos_tag(text)
   
   chunk_rst=ne_chunk(rst)
   
   for item in chunk_rst:
      if(hasattr(item,'label')):
         if item.label()=="PERSON":
            
            if(len(item)>1):
                if item[0][0].lower()==potentialWinner.lower():
                    rst=item[0][0]+" "+item[1][0]
                    #print(item[0][0]+" "+item[1][0])
                    return rst
                  
                #else:
                    #print("not exist")
                elif item[1][0].lower()==potentialWinner.lower():
                     rst=item[0][0]+" "+item[1][0]
                     #print(item[0][0]+" "+item[1][0])
                     return rst
                    
              
def isPartOfAwardName(winner):
    if winner.lower() in kwdList:
        return True
    else:
        return False

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

def getusername(handle):
    try:
        raw_data = urllib2.urlopen("https://twitter.com/search?q=%40" + handle).read()
        scripted_html = re.split(">",re.split('ProfileNameTruncated-link u-textInheritColor js-nav js-action-profile-name',raw_data)[1])
        untrimmed_name = re.split("<",scripted_html[1])
        trimmed_name = re.split("\n",untrimmed_name[0])
        return trimmed_name[1].strip()
    except:
        return handle

tweets_file = open('./goldenglobes.tab', "r")
first_names_path = './names.txt'
tweets_data = []

extr1 = ['actor', 'actress', 'performance']
extr2 = ['motion picture', 'supporting role', 'television series', 'limited series', '(Television|television|Tv|tv)']
extr3 = ['drama', 'musical or comedy', 'motion picture', '(Television|television|Tv|tv) movie']
extr4 = ['actor', 'actress', 'best', 'picture', 'drama', 'musical', 'comedy', 'director', 'motion', 'screenplay', 'animated', 'foreign', 'language', 'original', 'score', 'song', 'tv', 'television', 'series', 'limited', 'movie']
extr5 = ['donald', 'trump', 'powerful', 'speech']
winner_count = 0

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']

for tweet in tweets_file:
    tweets_data.append(tweet)

first_names = []
stop_words = set(stopwords.words('english'))
first_names_file = open(first_names_path,"r")
for name in first_names_file:
    try:
        first_names.append(re.split('\n',name)[0])
    except:
        continue

all_list1 = []
all_list2 = []


list1 = []
for element in tweets_data:
    m = re.compile("(.* nominated for.* Best.*)")

    try:
        if m.match(element):
            list1.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list1:
    split_tweet = re.split(' nominated for.* Best ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


list2 = []
for element in tweets_data:
    m = re.compile("(.* nominee for.* Best.*)")

    try:
        if m.match(element):
            list2.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list2:
    split_tweet = re.split(' nominee for.* Best ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)

list3 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* best.*)")

    try:
        if m.match(element):
            list3.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list3:
    split_tweet = re.split(' nomin.* best ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


list4 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* Best.*)")

    try:
        if m.match(element):
            list4.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list4:
    split_tweet = re.split(' nomin.* Best ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


list5 = []
for element in tweets_data:
    m = re.compile("(.* Nomin.* Best.*)")

    try:
        if m.match(element):
            list5.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list5:
    split_tweet = re.split(' Nomin.* Best ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


list6 = []
for element in tweets_data:
    m = re.compile("(.* Nomin.* Best.*)")

    try:
        if m.match(element):
            list6.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list6:
    split_tweet = re.split(' Nomin.* Best ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


list7 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* in.*)")

    try:
        if m.match(element):
            list7.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list7:
    split_tweet = re.split(' nomin.* in ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)

list8 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* of.*)")

    try:
        if m.match(element):
            list8.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list8:
    split_tweet = re.split(' nomin.* of ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


list9 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* of.*)")

    try:
        if m.match(element):
            list9.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list9:
    split_tweet = re.split(' nomin.* of ', tweet)
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    
    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    
    nominees = []
    temp1 = []
    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
        temp1.append(getusername(handle))
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                    temp1.append(chunk[0][0] + ' ' + chunk[1][0]) # added
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
                    temp1.append(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        temp2 = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
                temp2.append(w)
        
        if len(temp2) > 0:
            all_list1.append(temp1)
            all_list2.append(temp2)


## NOMINEES APPEARED ##
# 1. Best Performance by an Actress in a Motion Picture - Drama
# Amy Adams, Ruth Negga, Natalie Portman

# 2. Best Performance by an Actor in a Motion Picture - Drama
# Casey Affleck, Andrew Garfield, Denzel Washington

# 3. Best Performance by an Actress in a Motion Picture - Musical or Comedy
# Emma Stone, Lily Collins, Hailee Steinfeld, Meryl Streep

# 4. Best Performance by an Actor in a Motion Picture - Musical or Comedy
# Ryan Gosling, Colin Farrell, Ryan Reynolds

# 5. Best Performance by an Actress in a Supporting Role in any Motion Picture
# Viola Davis, Naomie Harris, Octavia Spencer, Michelle Williams

# 6. Best Performance by an Actor in a Supporting Role in any Motion Picture
# Dev Patel

# 7. Best Performance by an Actress in a Limited Series or a Motion Picture Made for Television
# Charlotte Rampling

# 8. Best Performance by an Actor in a Limited Series or a Motion Picture Made for Television
# Courtney B. Vance

# 9. Best Performance by an Actress In A Television Series - Drama
# Claire Foy, Caitriona Balfe, Evan Rachel Wood

# 10. Best Performance by an Actor In A Television Series - Drama


# 11. Best Performance by an Actress in a Television Series - Musical or Comedy
# Tracee Ellis Ross, Issa Rae, Gina Rodriguez

# 12. Best Performance by an Actor in a Television Series - Musical or Comedy
# Gael Garcia Bernal

# 13. Best Performance by an Actress in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television
# Lena Headey, Mandy Moore, Thandie Newton

# 14. Best Performance by an Actor in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television
# Sterling K. Brown, John Lithgow

# 15. Best Motion Picture - Drama
# Moonlight, Hell or High Water, Lion, Manchester by the Sea, Hacksaw Ridge

# 16. Best Motion Picture - Musical or Comedy
# La La Land, 20th Century Women, Deadpool, Florence Foster Jenkins, Sing Street

# 17. Best Director - Motion Picture
# Mel Gibson

# 18. Best Screenplay - Motion Picture


# 19. Best Motion Picture - Animated
# Sing

# 20. Best Motion Picture - Foreign Language


# 21. Best Original Score - Motion Picture
# Johann Johannsson, (Hans Zimmer, Pharrell Williams, Benjamin Wallfisch)

# 22. Best Original Song - Motion Picture


# 23. Best Television Series - Drama


# 24. Best Television Series - Musical or Comedy


# 25. Best Television Limited Series or Motion Picture Made for Television


# 26. Cecil B. DeMille Award



print "=============================== ALL THE NOMINEES ==============================="
a = len(all_list1)
temp = []
new1 = []
new2 = []
for i in range(0, a):
    if all_list1[i] not in temp:
        new1.append(all_list1[i])
        new2.append(all_list2[i])
        temp.append(all_list1[i])

print len(new1)
print len(new2)


count_nominee = 1
a = len(new1)
for i in range(0, a):
    print str(count_nominee) + '. ' + ' '.join(new1[i]) + ' was nominated for the award for Best ' + ' '.join(new2[i])
    count_nominee = count_nominee + 1



print "total nominees = " + str(count_nominee)
print "total appeared nominees = " + str(45)
rate = float(45) / count_nominee
print "Accuracy Rate = " + str(rate)




## ALL NOMINEES ##
# 1. Best Performance by an Actress in a Motion Picture - Drama
# Isabelle Huppert, Amy Adams, Jessica Chastain, Ruth Negga, Natalie Portman

# 2. Best Performance by an Actor in a Motion Picture - Drama
# Casey Affleck, Joel Edgerton, Andrew Garfield, Viggo Mortensen, Denzel Washington

# 3. Best Performance by an Actress in a Motion Picture - Musical or Comedy
# Emma Stone, Annette Bening, Lily Collins, Hailee Steinfeld, Meryl Streep

# 4. Best Performance by an Actor in a Motion Picture - Musical or Comedy
# Ryan Gosling, Colin Farrell, Hugh Grant, Jonah Hill, Ryan Reynolds

# 5. Best Performance by an Actress in a Supporting Role in any Motion Picture
# Viola Davis, Naomie Harris, Nicole Kidman, Octavia Spencer, Michelle Williams

# 6. Best Performance by an Actor in a Supporting Role in any Motion Picture
# Aaron Taylor-Johnson, Mahershala Ali, Jeff Bridges, Simon Helberg, Dev Patel

# 7. Best Performance by an Actress in a Limited Series or a Motion Picture Made for Television
# Sarah Paulson, Riley Keough, Charlotte Rampling, Kerry Washington, Felicity Huffman

# 8. Best Performance by an Actor in a Limited Series or a Motion Picture Made for Television
# Tom Hiddleston, Riz Ahmed, Bryan Cranston, John Turturro, Courtney B. Vance

# 9. Best Performance by an Actress In A Television Series - Drama
# Claire Foy, Caitriona Balfe, Keri Russell, Winona Ryder, Evan Rachel Wood

# 10. Best Performance by an Actor In A Television Series - Drama
# Billy Bob Thornton, Rami Malek, Bob Odenkirk, Matthew Rhys, Liev Schreiber

# 11. Best Performance by an Actress in a Television Series - Musical or Comedy
# Tracee Ellis Ross, Rachel Bloom, Julia Louis-Dreyfus, Sarah Jessica Parker, Issa Rae, Gina Rodriguez

# 12. Best Performance by an Actor in a Television Series - Musical or Comedy
# Donald Glover, Anthony Anderson, Gael Garcia Bernal, Nick Nolte, Jeffrey Tambor

# 13. Best Performance by an Actress in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television
# Olivia Colman, Lena Headey, Chrissy Metz, Mandy Moore, Thandie Newton

# 14. Best Performance by an Actor in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television
# Hugh Laurie, Sterling K. Brown, John Lithgow, Christian Slater, John Travolta
# 15. Best Motion Picture - Drama
# Moonlight, Hell or High Water, Lion, Manchester by the Sea, Hacksaw Ridge

# 16. Best Motion Picture - Musical or Comedy
# La La Land, 20th Century Women, Deadpool, Florence Foster Jenkins, Sing Street

# 17. Best Director - Motion Picture
# Damien Chazelle, Tom Ford, Mel Gibson, Barry Jenkins, Kenneth Lonergan

# 18. Best Screenplay - Motion Picture
# Damien Chazelle, Tom Ford, Barry Jenkins, Kenneth Lonergan, Taylor Sheridan

# 19. Best Motion Picture - Animated
# Zootopia, Moana, My Life as a Zucchini, Sing, Kubo and the Two Strings

# 20. Best Motion Picture - Foreign Language
# Elle, Divines, Neruda, The Salesman, Toni Erdmann

# 21. Best Original Score - Motion Picture
# Justin Hurwitz, Nicholas Britell, Johann Johannsson, (Dustin O'Halloran, Hauschka), (Hans Zimmer, Pharrell Williams, Benjamin Wallfisch)

# 22. Best Original Song - Motion Picture
# (City of Stars, Justin Hurwitz, Benj Pasek, Justin Paul), (Can't Stop the Feeling!), Faith, Gold, (How Far I'll Go)

# 23. Best Television Series - Drama
# The Crown, Game of Thrones, Stranger Things, This Is Us, Westworld

# 24. Best Television Series - Musical or Comedy
# Atlanta, Black-ish, Mozart in the Jungle, Transparent, Veep

# 25. Best Television Limited Series or Motion Picture Made for Television
# (The People v. O.J. Simpson: American Crime Story), American Crime, The Dresser, The Night Manager, The Night Of

# 26. Cecil B. DeMille Award
# Meryl Streep
