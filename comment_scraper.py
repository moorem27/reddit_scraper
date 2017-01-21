#!/usr/bin/python

import datetime
import codecs
import praw
import sys

# Map of a few politician names
politician_map = { "clinton" : 0,
                   "trump"   : 0,
                   "sanders" : 0,
                   "obama"   : 0 }


# Sample client_id, client_secret, password, username and user_agent (Replace these)
reddit = praw.Reddit(client_id='dasdfDfhd7lsfdalk',
                     client_secret='FDLddsklfFsdjfasdlfkjaDF',
                     password='password',
                     username='username',
                     user_agent='user_agent')

# Verify authentication
print(reddit.user.me())

# If an argument was passed in:
if len(sys.argv) > 1:
    # For each argument do:
    for a in sys.argv:
        # Skip over program name
        if( a != sys.argv[0] ):
            sub = reddit.subreddit(a)
            top_posts = sub.hot( params={'t':'year'}, limit=1000 )
            # For each submission ID in the top posts
    	    for sub_id in top_posts:
		# Create a submission from the ID
                submission = reddit.submission(id=sub_id)
		print(submission.title)
                submission.comments.replace_more(limit=0)
                # Perform breadth-first traversal of comments and replies (using list())
                for comment in submission.comments.list():
                    text = (comment.body).encode( 'utf-8' ).strip()
                    for name in politician_map:
			# If a name in the map matches any part of comment
			# increment the count for that name
                        if name in str(text).lower():
                            politician_map[ name ] += 1

	    # Print the output
            print "/r/" + str(sub) + ":"        
            for name in politician_map:
                print name.title(), politician_map[ name ]
                politician_map[ name ] = 0
















