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
for element in tweets_data:
    m = re.match(".*" + extr1[1] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[0] + ".*", element)
    try:
        if m:
            list1.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list1:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[0].title() + " - " + extr3[0].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list2 = []
for element in tweets_data:
    m = re.match(".*" + extr1[0] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[0] + ".*", element)
    try:
        if m:
            list2.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list2:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list2))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[0].title() + " - " + extr3[0].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list3 = []
for element in tweets_data:
    m = re.match(".*" + extr1[1] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[1].split(' ')[0] + ".*"+ extr3[1].split(' ')[2] + ".*", element)
    try:
        if m:
            list3.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list3:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list3))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[0].title() + " - " + extr3[1].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list4 = []
for element in tweets_data:
    m = re.match(".*" + extr1[0] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[1].split(' ')[0] + ".*"+ extr3[1].split(' ')[2] + ".*", element)
    try:
        if m:
            list4.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list4:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list4))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[0].title() + " - " + extr3[1].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list5 = []
for element in tweets_data:
    m = re.match(".*" + extr1[1] + ".*" + extr2[1].split(' ')[0] + ".*" + extr2[1].split(' ')[1] + ".*" + extr3[2].split(' ')[0] + ".*"+ extr3[2].split(' ')[1] + ".*", element)
    try:
        if m:
            list5.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list5:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list5))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
if (not nameDic) : 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list6 = []
for element in tweets_data:
    m = re.match(".*" + extr2[1].split(' ')[0] + ".*" + extr1[0] + ".*" + extr3[2].split(' ')[0] + ".*"+ extr3[2].split(' ')[1] + ".*", element)
    try:
        if m:
            list6.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list6:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list6))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list7 = []
for element in tweets_data:
    m = re.match(".*" + extr1[1] + ".*" + extr2[3].split(' ')[0] + ".*" + extr2[3].split(' ')[1] + ".*" + extr3[3].split(' ')[0] + ".*" + extr3[3].split(' ')[1] + ".*", element)
    try:
        if m:
            list7.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list7:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list7))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[3].title() + " - " + extr3[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list8 = []
for element in tweets_data:
    m = re.match(".*" + extr1[0] + ".*" + extr2[3].split(' ')[0] + ".*" + extr2[3].split(' ')[1] + ".*" + extr3[3].split(' ')[0] + ".*" + extr3[3].split(' ')[1] + ".*", element)
    try:
        if m:
            list8.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list8:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list8))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[3].title() + " - " + extr3[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list9 = []
for element in tweets_data:
    m = re.match(".*" + extr1[1] + ".*" + extr2[2] + ".*" + extr3[0] + ".*", element)
    try:
        if m:
            list9.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list9:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list9))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[2].title() + " - " + extr3[0].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list10 = []
for element in tweets_data:
    m = re.match(".*(" + extr1[0] + "|" + extr1[0].title() + ").*" + extr2[4] + ".*(" + extr3[0] + "|" + extr3[0].title() + ").*", element)
    try:
        if m:
            list10.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list10:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list10))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[2].title() + " - " + extr3[0].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list11 = []
for element in tweets_data:
    m = re.match(".*(" + extr1[1] + "|" + extr1[1].title() + ").*" + extr2[4] + ".*(" + extr2[2].split(' ')[1] + "|" + extr2[2].split(' ')[1].title() + ").*(" + extr3[1].split(' ')[0] + "|" + extr3[1].split(' ')[0].title() + ").*(" + extr3[1].split(' ')[2] + "|" + extr3[1].split(' ')[2].title() + ").*", element)
    try:
        if m:
            list11.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list11:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list11))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[2].title() + " - " + extr3[1].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list12 = []
for element in tweets_data:
    m = re.match(".*(" + extr1[0] + "|" + extr1[0].title() + ").*" + extr2[4] + ".*(" + extr2[2].split(' ')[1] + "|" + extr2[2].split(' ')[1].title() + ").*(" + extr3[1].split(' ')[0] + "|" + extr3[1].split(' ')[0].title() + ").*(" + extr3[1].split(' ')[2] + "|" + extr3[1].split(' ')[2].title() + ").*", element)
    try:
        if m:
            list12.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list12:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list12))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[2].title() + " - " + extr3[1].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list13 = []
for element in tweets_data:
    m = re.match(".*(" + extr2[1].split(' ')[0] + "|" + extr2[1].split(' ')[0].title() + ").*(" + extr1[1] + "|" + extr1[1].title() + ").*(" + extr2[3].split(' ')[0] + "|" + extr2[3].split(' ')[0].title() + ").*(" + extr2[3].split(' ')[1] + "|" + extr2[3].split(' ')[1].title() + ").*", element)
    try:
        if m:
            list13.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list13:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list13))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list14 = []
for element in tweets_data:
    m = re.match(".*(" + extr2[1].split(' ')[0] + "|" + extr2[1].split(' ')[0].title() + ").*(" + extr1[0] + "|" + extr1[0].title() + ").*(" + extr2[3].split(' ')[0] + "|" + extr2[3].split(' ')[0].title() + ").*(" + extr2[3].split(' ')[1] + "|" + extr2[3].split(' ')[1].title() + ").*", element)
    try:
        if m:
            list14.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list14:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list14))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list15 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*(" + extr4[4] + "|" + extr4[4].title() + ").*", element)
    try:
        if m:
            list15.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list15:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list15))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[8].title() + " " + extr4[3].title() + " - " + extr4[4].title()
#if (not nameDic): 
print "Winner : " + ' '.join(result)
#else:
#    print ("Winner : " + final_rst)



list16 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*(" + extr4[5] + "|" + extr4[5].title() + ").*(" + extr4[6] + "|" + extr4[6].title() + ").*", element)
    try:
        if m:
            list16.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list16:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list16))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[8].title() + " " + extr4[3].title() + " - " + extr4[5].title() + " or " + extr4[6].title()
#if (not nameDic): 
print "Winner : " + ' '.join(result)
#else:
#    print ("Winner : " + final_rst)



list17 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[7] + "|" + extr4[7].title() + ").*(" + extr4[8] + "|" + extr4[8].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*", element)
    try:
        if m:
            list17.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list17:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list17))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[7].title() + " - " + extr4[8].title() + " " + extr4[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list18 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[9] + "|" + extr4[9].title() + ").*(" + extr4[8] + "|" + extr4[8].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*", element)
    try:
        if m:
            list18.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list18:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list18))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[9].title() + " - " + extr4[8].title() + " " + extr4[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list19 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[8] + "|" + extr4[8].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*(" + extr4[10] + "|" + extr4[10].title() + ").*", element)
    try:
        if m:
            list19.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list19:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list19))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[8].title() + " " + extr4[3].title() + " - " + extr4[10].title()
#if (not nameDic): 
print "Winner : " + ' '.join(result)
#else:
#    print ("Winner : " + final_rst)



list20 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[8] + "|" + extr4[8].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*(" + extr4[11] + "|" + extr4[11].title() + ").*(" + extr4[12] + "|" + extr4[12].title() + ").*", element)
    try:
        if m:
            list20.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list20:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list20))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[8].title() + " " + extr4[3].title() + " - " + extr4[11].title() + " " + extr4[12].title()
#if (not nameDic): 
print "Winner : " + ' '.join(result)
#else:
#    print ("Winner : " + final_rst)



list21 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[13] + "|" + extr4[13].title() + ").*(" + extr4[14] + "|" + extr4[14].title() + ").*(" + extr4[8] + "|" + extr4[8].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*", element)
    try:
        if m:
            list21.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list21:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list21))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[13].title() + " " + extr4[14].title() + " - " + extr4[8].title() + " " + extr4[3].title()
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)



list22 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[13] + "|" + extr4[13].title() + ").*(" + extr4[15] + "|" + extr4[15].title() + ").*(" + extr4[8] + "|" + extr4[8].title() + ").*(" + extr4[3] + "|" + extr4[3].title() + ").*", element)
    try:
        if m:
            list22.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list22:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list22))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[13].title() + " " + extr4[15].title() + " - " + extr4[8].title() + " " + extr4[3].title()
# if (not nameDic): 
print "Winner : " + ' '.join(result)
# else:
    # print ("Winner : " + final_rst)



list23 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[16] + "|" + extr4[16].title() + "|" + extr4[17] + "|" + extr4[17].title() + ").*(" + extr4[18] + "|" + extr4[18].title() + ").*(" + extr4[4] + "|" + extr4[4].title() + ").*", element)
    try:
        if m:
            list23.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list23:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list23))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[17].title() + " " + extr4[18].title() + " - " + extr4[4].title()
#if (not nameDic): 
print "Winner : " + ' '.join(result)
#else:
#    print ("Winner : " + final_rst)



list24 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr4[16] + "|" + extr4[16].title() + "|" + extr4[17] + "|" + extr4[17].title() + ").*(" + extr4[18] + "|" + extr4[18].title() + ").*(" + extr4[5] + "|" + extr4[5].title() + ").*(" + extr4[6] + "|" + extr4[6].title() + ").*", element)
    try:
        if m:
            list24.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list24:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list24))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[17].title() + " " + extr4[18].title() + " - " + extr4[5].title() + " or " + extr4[6].title()
#if (not nameDic): 
print "Winner : " + ' '.join(result)
#else:
#    print ("Winner : " + final_rst)



list25 = []
for element in tweets_data:
    m = re.match(".*(" + extr4[2] + "|" + extr4[2].title() + ").*(" + extr2[4] + ").*(" + extr2[3].split(' ')[0] + "|" + extr2[3].split(' ')[0].title() + ").*(" + extr2[3].split(' ')[1] + "|" + extr2[3].split(' ')[1].title() + ").*", element)
    try:
        if m:
            list25.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list25:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list25))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Best " + extr4[17].title() + " " + extr4[19].title() + " or " + extr4[8].title() + " " + extr4[3].title() + " For " + extr4[17].title()
# if (not nameDic): 
print "Winner : " + ' '.join(result)
# else:
    # print ("Winner : " + final_rst)



list26 = []
for element in tweets_data:
    m = re.match(".*(" + extr5[0] + "|" + extr5[0].title() + ").*(" + extr5[1] + "|" + extr5[1].title() + ").*(" + extr5[2] + "|" + extr5[2].title() + ").*(" + extr5[3] + "|" + extr5[3].title() + ").*", element)
    try:
        if m:
            list26.append(m.group(0))
    except:
        continue

tf = Counter()
for tweet in list26:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

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
            A = Counter(trackNameBackinTweet(winner,list26))
            B = Counter(nameDic)
            C=A+B
            nameDic=C
            
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            if(check_count==2):
                break

final_rst=getPotentialWinner(nameDic)
print str(winner_count) + ". Cecil B. DeMille Award"
if (not nameDic): 
    print "Winner : " + ' '.join(result)
else:
    print ("Winner : " + final_rst)




