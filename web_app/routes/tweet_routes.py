# web_app/routes/home_routes.py


from flask import Blueprint, jsonify, request, render_template


from web_app.models import parse_records, Tweet, db


tweet_routes = Blueprint("tweet_routes", __name__)


@tweet_routes.route("/tweets")
def list_tweets():
    tweet_records = Tweet.query.all()
    print(tweet_records)

    tweets = parse_records(tweet_records)

    return render_template("tweets.html", message="Here are the tweets", tweets=tweets)


# @home_routes.route("/about")
# def about():
#     return "About me"
