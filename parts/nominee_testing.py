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

tweets_file = open('./goldenglobes.tab', "r")
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








list1 = []
list2 = []
for element in tweets_data:
    # m = re.match(".*" + extr1[1] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[0] + ".*", element)
    m = re.match(".*(Actress|actress).*(Motion|motion).*(Picture|picture).*(Drama|drama).*", element)
    # m = re.match(".*(Amy|amy|Adams|adams).*", element)
    try:
        if m:
            list1.append(m.group(0))
    except:
        continue

for i in list1:
    print i


print "================================="
for element in list1:
    m = re.match(".*nomin(ee|ees|ate|ated|ation).*", element)
    try:
        if m:
            list2.append(m.group(0))
    except:
        continue

for i in list2:
    print i

print "+=+++++++++++++++++++++++"
tf = Counter()
for tweet in list2:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for i in range(20):
    print tf.most_common()[i][0]

winner_count = winner_count + 1
check_count = 0;
result = []
nameDic = {}
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if isPartOfAwardName(winner):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            A = Counter(trackNameBackinTweet(winner,list1))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Nominees Best Performance By An " + extr1[1].title() + " In A " + extr2[0].title() + " - " + extr3[0].title()

print "Nominees : " + ' '.join(result)

print ("Nominees : " + final_rst)




