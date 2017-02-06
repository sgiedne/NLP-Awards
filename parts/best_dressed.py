import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import numpy
from collections import Counter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

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

#Count how many colors there are
N = len(frequency)

#Create an array with the color frequencies
color_frequencies = []
for value, count in frequency.most_common(10):
    color_frequencies.append(count)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, color_frequencies, width, color='#d62728')

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))

plt.show()






