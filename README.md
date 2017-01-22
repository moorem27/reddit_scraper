# Description  

The following scripts are used to parse various subreddit submission titles  
and comments. 


# Installation
  
$ sudo apt install python-pip  
$ pip install praw  
$ pip install --upgrade pip  
$ chmod +x scraper.py  

## Note:
Read the documentation on 'Authenticating via OAuth' at https://praw.readthedocs.io/en/latest.   
After following instructions provided by the link, the 'client_id', 'client_secret', 'password',   
'username', and 'user_agent' fields need to be updated in both scripts before use   
(Note: Be careful not to push your Reddit username and password to GitHub)  


## Sample output for searching submission titles for these names   

$ ./title_scraper.py   
USERNAME  
/r/Centrist:  
Sanders 3  
Clinton 8  
Trump 25  
Obama 5  
  
/r/democrats:  
Sanders 12  
Clinton 34  
Trump 40  
Obama 41  
  
## Search for the following names in the Politics subreddit submission comments  
(Pass subreddit(s) as a command line argument)  
  
$ ./comment_scraper.py Politics    
USERNAME  
/r/Politics  
Sanders 243  
Clinton 2095  
Trump 10934  
Obama 3087  
  
  
