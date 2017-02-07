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

kwdList=[kwdA1,kwdA2,kwdB1,kwdB2,kwdB3,kwdB4,kwdB5,kwdB6,kwdB7,kwdB8,kwdC1,kwdC2,kwdC3,kwdC4,kwdC5,kwdC6,kwdC7,kwdC8,kwdC9,kwdC10,kwdC11,kwdC12,kwdD1,kwdD2,kwdD3,kwdD4,kwdD5,kwdD6,kwdD7,kwdD8,kwdD9,kwdD10]
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
winner_count = 0

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']

for tweet in tweets_file:
    tweets_data.append(tweet)



# list1 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[1] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[0] + ".*", element)
#     try:
#         if m:
#             list1.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list1:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[0].title() + " - " + extr3[0].title()
# print "Winner : " + ' '.join(result)



# list2 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[0] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[0] + ".*", element)
#     try:
#         if m:
#             list2.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list2:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[0].title() + " - " + extr3[0].title()
# print "Winner : " + ' '.join(result)



# list3 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[1] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[1].split(' ')[0] + ".*"+ extr3[1].split(' ')[2] + ".*", element)
#     try:
#         if m:
#             list3.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list3:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[0].title() + " - " + extr3[1].title()
# print "Winner : " + ' '.join(result)



# list4 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[0] + ".*" + extr2[0].split(' ')[0] + ".*" + extr2[0].split(' ')[1] + ".*" + extr3[1].split(' ')[0] + ".*"+ extr3[1].split(' ')[2] + ".*", element)
#     try:
#         if m:
#             list4.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list4:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[0].title() + " - " + extr3[1].title()
# print "Winner : " + ' '.join(result)



# list5 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[1] + ".*" + extr2[1].split(' ')[0] + ".*" + extr2[1].split(' ')[1] + ".*" + extr3[2].split(' ')[0] + ".*"+ extr3[2].split(' ')[1] + ".*", element)
#     try:
#         if m:
#             list5.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list5:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# print "Winner : " + ' '.join(result)



# list6 = []
# for element in tweets_data:
#     m = re.match(".*" + extr2[1].split(' ')[0] + ".*" + extr1[0] + ".*" + extr3[2].split(' ')[0] + ".*"+ extr3[2].split(' ')[1] + ".*", element)
#     try:
#         if m:
#             list6.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list6:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# print "Winner : " + ' '.join(result)



# list7 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[1] + ".*" + extr2[3].split(' ')[0] + ".*" + extr2[3].split(' ')[1] + ".*" + extr3[3].split(' ')[0] + ".*" + extr3[3].split(' ')[1] + ".*", element)
#     try:
#         if m:
#             list7.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list7:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[3].title() + " - " + extr3[3].title()
# print "Winner : " + ' '.join(result)



# list8 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[0] + ".*" + extr2[3].split(' ')[0] + ".*" + extr2[3].split(' ')[1] + ".*" + extr3[3].split(' ')[0] + ".*" + extr3[3].split(' ')[1] + ".*", element)
#     try:
#         if m:
#             list8.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list8:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[3].title() + " - " + extr3[3].title()
# print "Winner : " + ' '.join(result)



# list9 = []
# for element in tweets_data:
#     m = re.match(".*" + extr1[1] + ".*" + extr2[2] + ".*" + extr3[0] + ".*", element)
#     try:
#         if m:
#             list9.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list9:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[2].title() + " - " + extr3[0].title()
# print "Winner : " + ' '.join(result)



# list10 = []
# for element in tweets_data:
#     m = re.match(".*(" + extr1[0] + "|" + extr1[0].title() + ").*" + extr2[4] + ".*(" + extr3[0] + "|" + extr3[0].title() + ").*", element)
#     try:
#         if m:
#             list10.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list10:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[2].title() + " - " + extr3[0].title()
# print "Winner : " + ' '.join(result)



# list11 = []
# for element in tweets_data:
#     m = re.match(".*(" + extr1[1] + "|" + extr1[1].title() + ").*" + extr2[4] + ".*(" + extr2[2].split(' ')[1] + "|" + extr2[2].split(' ')[1].title() + ").*(" + extr3[1].split(' ')[0] + "|" + extr3[1].split(' ')[0].title() + ").*(" + extr3[1].split(' ')[2] + "|" + extr3[1].split(' ')[2].title() + ").*", element)
#     try:
#         if m:
#             list11.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list11:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[2].title() + " - " + extr3[1].title()
# print "Winner : " + ' '.join(result)



# list12 = []
# for element in tweets_data:
#     m = re.match(".*(" + extr1[0] + "|" + extr1[0].title() + ").*" + extr2[4] + ".*(" + extr2[2].split(' ')[1] + "|" + extr2[2].split(' ')[1].title() + ").*(" + extr3[1].split(' ')[0] + "|" + extr3[1].split(' ')[0].title() + ").*(" + extr3[1].split(' ')[2] + "|" + extr3[1].split(' ')[2].title() + ").*", element)
#     try:
#         if m:
#             list12.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list12:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[2].title() + " - " + extr3[1].title()
# print "Winner : " + ' '.join(result)



# list13 = []
# for element in tweets_data:
#     m = re.match(".*(" + extr2[1].split(' ')[0] + "|" + extr2[1].split(' ')[0].title() + ").*(" + extr1[1] + "|" + extr1[1].title() + ").*(" + extr2[3].split(' ')[0] + "|" + extr2[3].split(' ')[0].title() + ").*(" + extr2[3].split(' ')[1] + "|" + extr2[3].split(' ')[1].title() + ").*", element)
#     try:
#         if m:
#             list13.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list13:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
# print "Winner : " + ' '.join(result)



# list14 = []
# for element in tweets_data:
#     m = re.match(".*(" + extr2[1].split(' ')[0] + "|" + extr2[1].split(' ')[0].title() + ").*(" + extr1[0] + "|" + extr1[0].title() + ").*(" + extr2[3].split(' ')[0] + "|" + extr2[3].split(' ')[0].title() + ").*(" + extr2[3].split(' ')[1] + "|" + extr2[3].split(' ')[1].title() + ").*", element)
#     try:
#         if m:
#             list14.append(m.group(0))
#     except:
#         continue

# tf = Counter()
# for tweet in list14:
#     try:
#         tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
#         tf.update(tokens)
#     except:
#         continue

# winner_count = winner_count + 1
# check_count = 0;
# result = []
# for i in range(20):
#     winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
#     check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
#     if isPartOfAwardName(winner):
#         continue
#     else:
#         if check_label and (check_count == 0 or check_count == 1):
#             check_count = check_count + 1
#             result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

# print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
# print "Winner : " + ' '.join(result)



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
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if isPartOfAwardName(winner):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
print "Winner : " + ' '.join(result)



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
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if isPartOfAwardName(winner):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
print "Winner : " + ' '.join(result)



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
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if isPartOfAwardName(winner):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
print "Winner : " + ' '.join(result)



list18 = []
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
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if isPartOfAwardName(winner):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))

print str(winner_count) + ". Best Performance By An " + extr1[0].title() + " In A " + extr2[1].title() + " - " + extr2[3].title()
print "Winner : " + ' '.join(result)














list17 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Director|director).*(Motion|motion).*(Picture|picture).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list17.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list17:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Director' or winner == 'Motion' or winner == 'Picture'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)









list18 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Screenplay|screenplay).*(Motion|motion).*(Picture|picture).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list18.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list18:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Screenplay' or winner == 'Motion' or winner == 'Picture'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)










list19 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Motion|motion).*(Picture|picture).*(Animated|animated).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list19.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list19:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Motion' or winner == 'Picture' or winner == 'Animated'):
        continue
    else:
        if check_label and (check_count == 0):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)








list20 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Motion|motion).*(Picture|picture).*(Foreign|foreign).*(Language|language).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list20.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list20:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Motion' or winner == 'Picture' or winner == 'Foreign' or winner == 'Language'):
        continue
    else:
        if check_label and (check_count == 0):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)










list21 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Original|original).*(Score|score).*(Motion|motion).*(Picture|picture).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list21.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list21:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Original' or winner == 'Score' or winner == 'Motion' or winner == 'Picture'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)








list22 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Original|original).*(Song|song).*(Motion|motion).*(Picture|picture).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list22.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list22:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Original' or winner == 'Song' or winner == 'Motion' or winner == 'Picture'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)









list23 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Tv|tv|Television|television).*(Series|series).*(Drama|drama).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list23.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list23:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Tv' or winner == 'Television' or winner == 'Series' or winner == 'Drama'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)








list24 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Best|best).*(Tv|tv|Television|television).*(Series|series).*(Musical|musical).*(Comedy|comedy).*", element)
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(Moon|moon).*(Light|light).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list24.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list15:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list24:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(20):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(20):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Tv' or winner == 'Television' or winner == 'Series' or winner == 'Musical' or winner == 'Comedy' or winner == 'Actress'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)







list25 = []
for element in tweets_data:
    # m = re.match(".*(Supporting|supporting).*(Actor|actor).*(Limited|limited).*(Series|series).*", element)
    m = re.match(".*(Limited|limited).*(Series|series).*(Tv|tv|Television|television).*(Movie|movie).*", element)
    # m = re.match(".*(Best|best).*(Crime|crime).*", element)
    
    # m = re.match(".*Olivia.*Colman.*", element)
    # m = re.match(".*(American|american).*(Crime|crime).*(Story|story).*", element)
    # m = re.match(".*(People|people).*(Simpson|simpson).*", element)
    # v = re.match(".*drama.*", element)
    
    try:
        # if v:
            # continue
        if m:
            list25.append(m.group(0))
    except:
        continue

print "[List of Frequency] Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
# for i in list25:
#     print i

tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct + ['rt', 'via']
tf = Counter()

for tweet in list25:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(30):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue


check_count = 0;
result = []
for i in range(30):
    winner = unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore')
    check_label = hasattr(ne_chunk(pos_tag(word_tokenize(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()).encode('ascii','ignore'))))[0], 'label')
    if (winner == 'Best' or winner == 'Tv' or winner == 'Television' or winner == 'Series' or winner == 'Musical' or winner == 'Comedy' or winner == 'Actress'):
        continue
    else:
        if check_label and (check_count == 0 or check_count == 1):
            check_count = check_count + 1
            result.append(unicodedata.normalize('NFKD', tf.most_common()[i][0].title()))
            # print

print "Best Performance By An " + extr1[1].title() + " In A " + extr2[1].title() + " - " + extr3[2].title()
print ' '.join(result)






















# print "TTTTTTTTTTTTTTTTTTTTTTTTT"
#     elif( pos_tag(word_tokenize(tf.most_common()[i][0].title()))[0][1] == 'NNP'):
#         continue
        
# print word_tokenize(tf.most_common()[0][0].title())
# print pos_tag(word_tokenize(tf.most_common()[0][0].title()))
# print pos_tag(word_tokenize(tf.most_common()[8][0].title()))[0][1]
# print pos_tag(word_tokenize(tf.most_common()[9][0].title()))[0][1] 
# print pos_tag(word_tokenize(tf.most_common()[10][0].title()))[0][1]
# print ne_chunk(pos_tag(word_tokenize(tf.most_common()[8][0].title())))
# print hasattr(ne_chunk(pos_tag(word_tokenize(tf.most_common()[8][0].title()))), 'label')
# print ne_chunk(pos_tag(word_tokenize(tf.most_common()[8][0].title()))).label()
# print "TTTTTTTTTTTTTTTTTTTTTTTTT"