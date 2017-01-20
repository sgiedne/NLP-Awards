#tweets_data_path = './goldenglobes.tab'

#tweets_data = []
#tweets_file = open(tweets_data_path, "r")
#for tweet in tweets_file:
#    try:
#        tweets_data.append(tweet)
        
      
#    except:
#        continue

#result=len(tweets_data)

#print (result)
#print("This line will be printed." )

#Ref:https://docs.python.org/2/library/csv.html

import csv

keyword="award"

results = []

  

with open('goldenglobes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if keyword in row['TweetText']:
             results.append(row['TweetText'])
           #print(row['TweetText'], row['TweetUserName'])




with open('result.csv', 'w') as csvfile:
    fieldnames = ['TweetText', 'id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
     
    for element in results:
         writer.writerow({'TweetText': element, 'id': 0})
  
   
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})