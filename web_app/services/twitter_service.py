
# python web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY", default="OOPS")
consumer_secret = os.getenv("TWITTER_API_SECRET", default="OOPS")
access_token = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print("AUTH", type(auth))

print("---------------")
print("---------------")
api = tweepy.API(auth)
print("API", type(api)) #<class 'tweepy.api.API'>
# pprint(dir(api))
# breakpoint() 

# get information about twitter user
screen_name ="dril"
user = api.get_user(screen_name)
print("USERNME:", user.screen_name)
print("# of FOLLOWRS:", user.followers_count)
pprint(user._json)
print("---------------")
print("---------------")

# get user tweets
# see: http://docs.tweepy.org/en/latest/api.html#API.user_timeline
print("STATUSES...")
statuses = api.user_timeline(screen_name, tweet_mode="extended", 
count=150, exclude_replies=True, include_rts=False)

for status in statuses:
     print(type(status)) # <class 'tweepy.models.Status'>
     print("---------------")
     print(status.full_text)