# This program outputs a graph with the most tweeted about dress colors
# at the Golden Globes (or any other award ceremony)

import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt; plt.rcdefaults()

# Get the tweet data and the color list 
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

# These are common color hexcodes used to make the graph
common_color_hexcodes = {'black': '#000000', 'gray': '#808080', 
                            'silver': '#C0C0C0', 'white': '#FFFFFF', 
                            'maroon': '800000', 'red': '#FF0000', 
                            'olive': '#808000', 'yellow': '#FFFF00', 
                            'green': '#008000', 'lime': '#00FF00', 
                            'teal': '#008080', 'aqua': '#00FFFF', 
                            'navy': '#000080', 'blue': '#0000FF', 
                            'purple': '#800080', 'fuschia': '#FF00FF'
                        }
default_color = '#000000'

# Collect all tweets that are related to colors of dresses
pattern = re.compile('.* dress.*')

# Go through all the relevant tweets
# If the word immediately before "dress" is a color in all_colors.txt, then add it to a list
colors_of_dresses = []

for tweet in tweets_data:
    try:
        if pattern.match(tweet):
        	split_tweet = re.split('dress', tweet)
        	tagged = pos_tag(word_tokenize(split_tweet[0]))

        	i = len(tagged) - 1

        	color_of_dress = list(tagged[i])

        	if color_of_dress[1] == 'JJ':
        		potential_color = str(color_of_dress[0])
        		if potential_color in color_list:
        			colors_of_dresses.append(potential_color)
    except:
        continue


frequency = Counter(colors_of_dresses) # count how frequently the colors are tweeted
N = len(frequency.most_common(10)) #count how many popular colors exist 

# Create arrays with the properties for the graph
color_frequencies = []
color_names = []
bar_colors = []
for value, count in frequency.most_common(10):
    color_frequencies.append(count)
    color_names.append(value)
    try: 
        if common_color_hexcodes.get(value):
            bar_colors.append(common_color_hexcodes.get(value))
    except:
        bar_colors.append(default_color)

# Function to choose an appropriate space between ticks
def choose_tick_diff(frequencylist):
    freq_range = max(frequencylist) - min (frequencylist)
    exponent = 0

    while freq_range > (10 ** exponent):
        exponent += 1
    
    return 10 ** (exponent-1)

# Setup and draw the graph 
width = 0.50       # the width of the bars
ind = np.arange(N)   # the x locations for the bars
tick_diff = choose_tick_diff(color_frequencies) # the space between ticks on the y-axis 

p = plt.bar(ind, color_frequencies, width, color=bar_colors, align='center', edgecolor='black')

plt.ylabel('Number of Tweets')
plt.title('The Most Tweeted About Dress Colors')
plt.xticks(ind, color_names)
plt.yticks(np.arange(0, max(color_frequencies), tick_diff))

plt.show()
