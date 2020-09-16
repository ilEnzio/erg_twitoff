# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api_client
from web_app.services.basilica_service import connection as basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)

    # Fetching data from twitter API
    twitter_user = twitter_api_client.get_user(screen_name)

    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count

    db.session.add(db_user)
    db.session.commit()
    # return "OK"
    # breakpoint()

    # Fetch Tweets!!!

    tweets = twitter_api_client.user_timeline(
        screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("STATUSES COUNT:", len(tweets))
    # return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    # basilica_api = basilica_api_client()

    all_tweet_texts = [tweet.full_text for tweet in tweets]
    num_embeddings = list(basilica_api_client.embed_sentences(
        all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(num_embeddings))

    # # TODO: explore using the zip() function maybe...

    for index, status in enumerate(tweets):
        num_embedding = num_embeddings[index]
    #   STORE TWEETS IN DATABASE
    # slow loop
    # for status in tweets:
    #     print(status.full_text)
    #     print("----")
    #     # print(dir(status))
    #     # get existing tweet from the db or initialize a new one:
    #     num_embedding = basilica_api_client.embed_sentence(
    #         status.full_text, model="twitter")
    #     print(len(num_embedding))

        db_tweet = Tweet.query.get(
            status.id) or Tweet(tweet_id=status.id)
        db_tweet.user_id = status.author.id  # or db_user.id
        db_tweet.text = status.full_text
        # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        # embedding = embeddings[counter]
        db_tweet.num_embedding = num_embedding
        db.session.add(db_tweet)

        db.session.commit()
    # # breakpoint()
    return "OK"
    # return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets
