import glob
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tweepy
import tweepy.streaming as ts
from tweepy import OAuthHandler, Stream
from tweepy import API
from tweepy import Stream
import pandas as pd

sid = SentimentIntensityAnalyzer()

# Fill blank spaces with your keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# Consumer key authentication(consumer_key,consumer_secret can be collected from our twitter developer profile)
auth = OAuthHandler(consumer_key, consumer_secret)

# Access key authentication(access_token,access_token_secret can be collected from our twitter developer profile)
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api = API(auth, wait_on_rate_limit=False)

# The word or trend you want to search
search_words = "#BreaktheHabit"

# items is no of tweets you want to fetch
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_words,
                       lang="en").items(300)

# creates a list and appends the text to list
dt = []
for tweet in tweets:
    dt.append(tweet.text)

# creates a pandas dataframe
df_tweet = pd.DataFrame(dt)
# Generate sentiment scores
sentiment_scores = df_tweet[0].apply(sid.polarity_scores)
sentiment = sentiment_scores.apply(lambda x: x['compound'])
# Prints all sentiment scores
print(sentiment_scores)
# Prints mean sentiment scores
sentiment_py = sentiment.mean()
print(sentiment_py)
