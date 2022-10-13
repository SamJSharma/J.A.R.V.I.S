import datetime
sentence = "My name is Sameera!"

words = sentence.split()

#print(words[0])
#print(len(words))

today = datetime.date.today()

print(today.day)

hour = int(datetime.datetime.now().minute)

#print(hour)

import googlesearch

#results = googlesearch.lucky("Flipkart")
#results2 = googlesearch.url_search("Ashish Chanchlani")
import webbrowser

#webbrowser.open(results)

time = "8:30"

#print(time.split())

#print(time[3])

#print(len(time))



now = (int(time[0])*1)+ ((((int(time[2]))*10)+(int(time[3])))/60)

#print(now)

result = googlesearch.search("amazon")
import os


os.open(result)