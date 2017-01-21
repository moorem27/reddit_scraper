#!/usr/bin/python

import datetime
import codecs
import praw

politician_map = { "clinton" : 0,
                   "trump"   : 0,
                   "sanders" : 0,
		   "obama"   : 0 }

sub_reddits = { "democrats", "Republican", "Politics",
		"Liberal", "Conservative", "Libertarian",
		"Socialism", "Progressive", "Labor",
		"Centrist", "Communism", "2016_elections",
		"Anarchism" }

post_limit = 1000
time = 'year'

#sample client_id, client_secret, password, username, and user_agent                                              
reddit = praw.Reddit(client_id='Dfxf324dssf',
		     client_secret='fDFDFLAK8felksdfjliesfdsa',
		     password='password',
		     username='username',	
	             user_agent='user_agent')


# Check if authenticated
print(reddit.user.me())

for s in sub_reddits:
	sub = reddit.subreddit(s)
	top_posts = sub.top( params={ 't': time }, limit=post_limit )
	
	for submissions in top_posts:
		title = ( submissions.title ).encode( 'utf-8' ).strip()
		words_in_title = str( title )

		for name in politician_map:
			if name in words_in_title.lower():
				politician_map[ name ] += 1

	print "/r/" + str( sub ) + ":"

	for name in politician_map:
		print name.title(), politician_map[ name ]
		politician_map[ name ] = 0

	print( "" )
