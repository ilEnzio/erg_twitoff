

import tweepy

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
import os
from dotenv import load_dotenv

from tweepy import OAuthHandler, API

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", auth)
api = API(auth)
print("API CLIENT", api)

# print(dir(api))
if __name__ == "__main__":
    user = api.get_user('DAVID_LYNCH')
    user02 = api.get_user("Hmscottjr")
    print("TWITTER USER:", type(user))

    tweets02 = api.user_timeline("Hmscottjr", tweet_mode="extended")
    tweets = api.user_timeline("DAVID_LYNCH", tweet_mode="extended")

    print(user02.id)
    print(user02.name)
    print(user02.screen_name)
    print(tweets02[0].full_text)

    print()
    print(user.id)
    print(user.name)
    print(user.screen_name)
    print(tweets[0].full_text)
    # breakpoint()


# if __name__ == "__main__":

#     api = get_twitter_api()
# Get the User object for twitter...
