import tweepy
import os
from dotenv import load_dotenv
from math import ceil
from typing import Callable
load_dotenv()

# twitter
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_KEY_SECRET = os.getenv("CONSUMER_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
MAX_CHARACTER = 258

def auth_to_twitter(consumer_key: str, consumer_key_secret: str, access_token: str, access_token_secret: str):
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def create_twitter_api_object(auth):
    return tweepy.API(auth)

def should_create_thread(quote: str) -> int:
    return ceil(len(quote) / MAX_CHARACTER) > 1

def tweet_new_quote(send_tweet: Callable[[str], object], quote: str, reply_tweet_id: str = None) -> object:
    formatted_quote = quote[0:MAX_CHARACTER]
    tweeted_quote = send_tweet(formatted_quote, reply_tweet_id)
    
    if should_create_thread(quote):
        tweet_new_quote(send_tweet, quote[MAX_CHARACTER:len(quote)], tweeted_quote.id_str)
    
    return tweeted_quote

auth = auth_to_twitter(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
TWITTER_API = create_twitter_api_object(auth)