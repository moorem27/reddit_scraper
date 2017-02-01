#!/usr/bin/python

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = ["I love Chipotle.", 
	     "That burrito was great.", 
             "Good job, you ruined the bathroom.", 
             "Mount Doom is smoldering.",
	     "Great, now I have food poisoning."]

sid = SentimentIntensityAnalyzer()

for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]) )
    print(' ')
	    

