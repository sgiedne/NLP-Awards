import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import numpy
from collections import Counter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

tweets_data_path = './goldenglobes.tab'
color_data_path = './all_colors.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

color_list = []
color_data_file = open(color_data_path, "r")

for tweet in tweets_file:
    try:
        tweets_data.append(tweet)
    except:
        continue

for color in color_data_file:
	try:
		color_list.append(re.split('\n', color)[0].lower())
	except:
		continue
        
colors_of_dresses = []

pattern = re.compile('.* dress.*')

for tweet in tweets_data:
    try:
        if pattern.match(tweet):
        	split_tweet = re.split('dress', tweet)
            #pos_tag these tweets
        	tagged = pos_tag(word_tokenize(split_tweet[0]))

        	i = len(tagged) - 1

        	color_of_dress = list(tagged[i])

        	if color_of_dress[1] == 'JJ':
        		potential_color = str(color_of_dress[0])
        		if potential_color in color_list:
        			colors_of_dresses.append(potential_color)
    except:
        continue

print "==========This is a count of the colors of dresses========="
frequency = Counter(colors_of_dresses)
print frequency.most_common(10)



objects = colors_of_dresses
y_pos = np.arange(len(objects))
i = 0
while i < len(objects):
	performance = objects[i][1]
	i+=1
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of tweets')
plt.title('Colors of Dresses')
 
plt.show()





