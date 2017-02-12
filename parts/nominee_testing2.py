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


print "=============================== CHECKS PATTERN ==============================="
list0 = []
for element in tweets_data:
    # m = re.match(".*(Actress|actress).*(Motion|motion).*(Picture|picture).*", element)
    # m = re.match(".*(Amy|amy|Adams|adams).*", element)
    # m = re.compile("(.* present.* Best.*)")
    # v = re.compile(".*(cli(p|ps)|nomin).*")

    # m = re.compile("((.*(Nomin|nomin).*(Best|best).*)|(.*(Best|best).*(Nomin|nomin).*))")
    # m = re.compile(".*(nominated for).*")
    # m = re.compile(".*(Isabelle|isabelle|Huppert|huppert).*");
    m = re.compile(".*(Jessica|jessica|Chastain|chastain).*");
    try:
        # if v.match(element):
            # continue
        if m.match(element):
            list0.append(element)
    except:
        continue

# for i in list0:
#     print i
list00 = []
for element in list0:
    # m = re.match(".*(Actress|actress).*(Motion|motion).*(Picture|picture).*", element)
    # m = re.match(".*(Amy|amy|Adams|adams).*", element)
    # m = re.compile("(.* present.* Best.*)")
    # v = re.compile(".*(cli(p|ps)|nomin).*")

    # m = re.compile("((.*(Nomin|nomin).*(Best|best).*)|(.*(Best|best).*(Nomin|nomin).*))")
    # m = re.compile(".*(nominated for).*")
    # m = re.compile(".*(Isabelle|isabelle|Huppert|huppert).*");
    m = re.compile(".*(Nomin|nomin).*");
    try:
        # if v.match(element):
            # continue
        if m.match(element):
            list00.append(element)
    except:
        continue

# for i in list00:
#     print i

print "=============================== CHECKS PATTERN ==============================="


print "=============================== CODE 1 STARTS HERE ==============================="

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

    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    # if (chunk[0][0] + ' ' + chunk[1][0]) in occurring_names or chunk[0][0] not in first_names:
                    #     continue
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    presenter.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
    
        if len(filtered_split_right) > 0:
            print ' '.join(nominees) + ' was nominated for the award for Best ' + ' '.join(filtered_split_right)
            print '--------------------------------------------------------------------------------'

print "=============================== CODE 1 ENDS HERE ==============================="
print "=============================== CODE 2 STARTS HERE ==============================="

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

    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    # print chunk[0][0] + ' ' + chunk[1][0]
                    # if (chunk[0][0] + ' ' + chunk[1][0]) in occurring_names or chunk[0][0] not in first_names:
                        # continue
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
    
        if len(filtered_split_right) > 0:
            print ' '.join(nominees) + ' was nominated for the award for Best ' + ' '.join(filtered_split_right)
            print '--------------------------------------------------------------------------------'

print "=============================== CODE 2 ENDS HERE ==============================="
print "=============================== CODE 3 STARTS HERE ==============================="

list3 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* best.*)")
    # m = re.compile("(.* nomin.* Best.*)")
    try:
        if m.match(element):
            list3.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list3:
    # split_tweet = re.split(' nominated.* for.* best ', tweet)
    split_tweet = re.split(' nomin.* best ', tweet)

    # chunk_left2 = split_tweet[0].replace('#', '')
    # print split_tweet[0]
    # print chunk_left2
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    # chunk_left = ne_chunk(pos_tag(word_tokenize(chunk_left2)))

    # print chunk_left

    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    # print split_right
    nominees = []

    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    # print chunk[0][0] + ' ' + chunk[1][0]
                    # if (chunk[0][0] + ' ' + chunk[1][0]) in occurring_names or chunk[0][0] not in first_names:
                        # continue
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
    
        if len(filtered_split_right) > 0:
            print ' '.join(nominees) + ' was nominated for the award for Best ' + ' '.join(filtered_split_right)
            print '--------------------------------------------------------------------------------'

print "=============================== CODE 3 ENDS HERE ==============================="
print "=============================== CODE 4 STARTS HERE ==============================="

list4 = []
for element in tweets_data:
    m = re.compile("(.* nomin.* Best.*)")
    # m = re.compile("(.* nomin.* Best.*)")
    try:
        if m.match(element):
            list4.append(element)
    except:
        continue

occurring_names = set()
occurring_handles = set()

for tweet in list4:
    # split_tweet = re.split(' nominated.* for.* best ', tweet)
    split_tweet = re.split(' nomin.* Best ', tweet)

    # chunk_left2 = split_tweet[0].replace('#', '')
    # print split_tweet[0]
    # print chunk_left2
    chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
    # chunk_left = ne_chunk(pos_tag(word_tokenize(chunk_left2)))

    # print chunk_left

    if len(split_tweet) > 1:
        split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
    # print split_right
    nominees = []

    if re.match('RT.*: ',split_tweet[0]):
        split_tweet_for_handles = re.split('RT.*: ',split_tweet[0])
        twitter_handles_left = re.findall(r"@(\w+)", split_tweet_for_handles[1])
        
    for handle in twitter_handles_left:
        if handle in occurring_handles:
            continue
        nominees.append(getusername(handle))
        occurring_handles.add(handle)
    
    for chunk in chunk_left:
        if hasattr(chunk,'label'):
            if chunk.label() == 'PERSON':
                if len(chunk) > 1:
                    # print chunk[0][0] + ' ' + chunk[1][0]
                    # if (chunk[0][0] + ' ' + chunk[1][0]) in occurring_names or chunk[0][0] not in first_names:
                        # continue
                    nominees.append(chunk[0][0] + ' ' + chunk[1][0])
                    occurring_names.add(chunk[0][0] + ' ' + chunk[1][0])
                else:
                    if chunk[0][0] in occurring_names or chunk[0][0] not in first_names:
                        continue
                    nominees.append(chunk[0][0])
                    occurring_names.add(chunk[0][0])
    
    if len(nominees) > 0:
        filtered_split_right = []
        for w in word_tokenize(split_right[0]):
            if w not in stop_words and re.match('[A-Z]',w[0]):
                filtered_split_right.append(w)
    
        if len(filtered_split_right) > 0:
            print ' '.join(nominees) + ' was nominated for the award for Best ' + ' '.join(filtered_split_right)
            print '--------------------------------------------------------------------------------'







# print "=============== TEST 1 ==============="
# print list1[0]
# print "=============== TEST 2 ==============="
# # split_tweet = re.split(" present.* Best ", list1[0])
# split_tweet = re.split(" nominated for.* Best ", list1[0])
# print split_tweet[0]
# print split_tweet[1]
# print "=============== TEST 3 ==============="
# chunk_left = ne_chunk(pos_tag(word_tokenize(split_tweet[0])))
# print chunk_left
# print "=============== TEST 4 ==============="
# print split_tweet[1]
# print "=============== TEST 5 ==============="
# split_right = re.split('#|\t|http|\.|,|@|\?|',split_tweet[1])
# print split_right[0]
# print split_right[1]
# print split_right[2]
# print split_right[3]
# print split_right[4]
# print "=============== TEST 6 ==============="
# # print occurring_handles
# # print occurring_handles[0]
# # print occurring_handles[1]
# print "=============== TEST 7 ==============="
# # print re.match('RT.*: ',split_tweet[0])
# print hasattr(chunk_left[4], 'label')
# print "=============== TEST 8 ==============="
# print chunk_left[4].label() == 'PERSON'
# print "=============== TEST 9 ==============="
# print len(chunk_left[4])
# print "=============== TEST 10 ==============="
# print chunk_left[4][0][0]
# print chunk_left[4][1][0]
# print "=============== TEST 11 ==============="