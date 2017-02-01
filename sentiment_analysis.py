#!/usr/bin/python

import datetime
import codecs
import praw
import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Sample client_id, client_secret, password, username and user_agent (Replace these)
reddit = praw.Reddit(client_id='client_id',
		     client_secret='client_secret',
                     password='password',
                     username='username',
                     user_agent='user_agent')

# Verify authentication
#print(reddit.user.me())

# Average sentiments
subreddit_sentiment  = 0

# Number of data points
n_subreddit  = 1

if len(sys.argv) > 1:
    # For each argument (subreddit)
    for a in sys.argv:
	# Skip over the program name
        if(a != sys.argv[0]):
            subreddit = reddit.subreddit(a)
	    print(subreddit)
	    hot_list = subreddit.hot(params={'t':'year'}, limit=1000)	    
	    # The current subreddit average
	    subreddit_average = 0
	    # For each submission in the subreddit
	    for sub_id in hot_list:
                submission = reddit.submission(id=sub_id)

	    	# Use new variables for the average
		comment_sentiment = 0
		comment_count = 0
		average = 0

		# Perform breadth-first traversal of comments and replies (using list())
		submission.comments.replace_more(limit=0)
                # For each comment in the submission calculate the sentiment 
                for comment in submission.comments.list():
                    comment_count += 1
                    text = str((comment.body).encode('utf-8').strip())
		    sid = SentimentIntensityAnalyzer()
		    ss = sid.polarity_scores(text)
		    
		    for k in sorted(ss):
			# Grab the comment sentiment and increment the total count
	                if(k == 'compound'):
                            comment_sentiment += ss[k]
	                    

		# Ensure that submission has comments
		if(comment_count > 0 and comment_sentiment > 0):
 		    average = comment_sentiment/comment_count
		# Increment the subreddit sentiment by the average of previous submissions
                subreddit_sentiment += average

		# Calculate subreddit average and increment number of subreddits counted so far
		subreddit_average = subreddit_sentiment/n_subreddit
		n_subreddit += 1

                # Uncomment the lines below to see progress while program runs
                #sys.stdout.write("subreddit_sentiment: " + str(subreddit_average) + "   \r")
         	#sys.stdout.flush()
            print("subreddit_sentiment: " + str(subreddit_average))
    # Clear average and count for subreddit before new subreddit
    subreddit_sentiment = 0
    n_subreddit = 0
    print(" ") 
