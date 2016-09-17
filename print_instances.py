#!/usr/bin/python

import datetime
import codecs
import praw

# Key:   Politician name
# Value: How many times their name appears in a submission title
politician_map = { "clinton" : 0,
                   "trump"   : 0,
                   "sanders" : 0 }

# List of a few political subreddits to scan
subreddits = { "democrats", "Republican", "Politics", 
               "Liberal", "Conservative", "Libertarian", 
               "Socialism", "Progressive", "Labor",
               "Centrist", "Communism", "2016_elections",
               "Anarchism" }

# Limit number of posts to search through
post_limit = 1000

# How far back to look (Examples: 'year', 'month', 'week', 'day')
time = 'year'

print( "The number of times these candidate last names have appeared in submission titles for the following subreddits " )
print( "(Going back " + str( post_limit ) + " posts in each subreddit in the past year)\n" )


# For every subreddit in the list
#     1. Scan over each subreddit's top posts
#     2. Convert the post title to a string
#     3. If any of the candidate names appear in the title, increment their count
#     4. Print the results for each candidate

# 1
for subreddit in subreddits:
    r = praw.Reddit('Title parser')
    subreddit = r.get_subreddit( subreddit )
    top_posts = subreddit.get_top( params={ 't': time }, limit=post_limit )

    # 2
    for submissions in top_posts:
        title = ( submissions.title ).encode( 'utf-8' ).strip()
        words_in_title = str( title )

        # 3 
        for name in politician_map:
            if name in words_in_title.lower():
                politician_map[ name ] += 1

    print "/r/" + str( subreddit ) + ":"

    # 4
    for name in politician_map:
        print name.title(),  politician_map[ name ]
        politician_map[ name ] = 0

    print( "" )
