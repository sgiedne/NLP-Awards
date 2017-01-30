import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.stem import PorterStemmer
import numpy
import string
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

tweets_file = open('./goldenglobes.tab', "r")
write_file = open('./write.tab', "w")
tweets_data = []
award_extract_1 = []
award_extract_2 = []
award_extract_3 = []
award_extract_4 = []

for tweet in tweets_file:
    tweets_data.append(tweet)

for element in tweets_data:
    m = re.match(".*(Best|best) (Performance|performance) (By|by) (An|an) (Actor|actor|Actress|actress).*", element)

    try:
        if m:
            award_extract_1.append(m.group(0))
            write_file.write(element)
            actor_list = element.lower().split(' best performance by an actor in a ')
            actress_list = element.lower().split(' best performance by an actress in a ')
            
            award_extract_2.append(re.split(' |, ', actor_list[1])[0] + ' ' + re.split(' |, ', actor_list[1])[1])
            award_extract_2.append(re.split(' |, ', actress_list[1])[0] + ' ' + re.split(' |, ', actress_list[1])[1])
    except:
        continue

print "==================== Award_Extract_1 START ===================="
frequency_1 = Counter(award_extract_2)
print frequency_1.most_common(10)
print frequency_1.most_common()[0][0]
print frequency_1.most_common()[1][0]
print frequency_1.most_common()[2][0]
print frequency_1.most_common()[3][0]
print frequency_1.most_common()[4][0]
print "==================== Award_Extract_1 END ===================="
    

print "==================== Award_Extract_2 START ===================="
str1 = frequency_1.most_common()[0][0].split(' ')[0]
str2 = frequency_1.most_common()[0][0].split(' ')[1]
str3 = frequency_1.most_common()[0][0].split(' ')[0].title()
str4 = frequency_1.most_common()[0][0].split(' ')[1].title()
for element in award_extract_1:
    m = re.match(".*(" + str1 + "|" + str2 + "|" + str3 + "|" + str4 + ").*", element)

    try:
        if m:
            genre_list = element.lower().split(' ' + frequency_1.most_common()[0][0] + ' ')            
            award_extract_3.append(genre_list[1])
    except:
        continue


tweet_tokenizer = TweetTokenizer()
punct = list(string.punctuation)
stopword_list = stopwords.words('english') + punct
tf = Counter()
for tweet in award_extract_3:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(10):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue

print tf.most_common(10)[0][0]
print tf.most_common(10)[1][0]
print tf.most_common(10)[2][0]
print tf.most_common(10)[3][0]
print tf.most_common(10)[4][0]
print "==================== Award_Extract_2 END ===================="


print "==================== Award_Extract_3 START ===================="
str1 = "actress"
str2 = frequency_1.most_common()[0][0].split()[0]
str3 = frequency_1.most_common()[0][0].split()[1]
str4 = tf.most_common(10)[4][0]    
str5 = ".*" + str1 + ".*" + str2 + ".*" + str3 + ".*" + str4 + ".*"

motion_picture_actress_winner = ""
for element in tweets_data:
    m = re.match(str5, element)

    try:
        if m:
            award_extract_4.append(m.group(0))

    except:
        continue

for tweet in award_extract_4:
    try:
        tokens = process(tweet, tokenizer=tweet_tokenizer, stopwords=stopword_list)
        tf.update(tokens)
    except:
        continue

for tag, count in tf.most_common(10):
    try:
        print("{}: {}".format(tag, count))
    except:
        continue

print "==================== Award_Extract_3 END ===================="


print "==================== Award_Extract_4 START ===================="

motion_picture_actress_winner = tf.most_common(10)[8][0] + " " + tf.most_common(10)[9][0]
print "Best Performance by an Actress in a Motion Picture - Drama"
print motion_picture_actress_winner

print "==================== Award_Extract_4 END ===================="
