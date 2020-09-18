# web_app/routes/stats_routes.py

from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegression  # for example

from web_app.models import User, Tweet
# from web_app.services.basilica_service import basilica_api_client

stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    # > {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    # these tweets are in the the db
    # so I need to load the num_embedding part as the X_matrix
    # then load the screenname as the y_target
    # oh we train the model on everything!

    print("-----------------")
    print("FETCHING TWEETS FROM THE DATABASE...")

    # TODO

    classifier = LogisticRegression()

    # TODO: classifier.fit(___________, ___________)
    #

    # sqlachemy docs to find a attribute from an object?

    user_a = User.query.filter_by(screen_name=screen_name_a).first()
    user_b = User.query.filter_by(screen_name=screen_name_b).first()

    # this works because of the db.relationship line in the Tweet Model.
    # that essential adds a tweets property/relationship  to each User.

    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets

    print(len(user_a_tweets))
    print(len(user_b_tweets))

    # so to get a list of Xmatrix I could say for each tweet in

    embeddings = []
    labels = []

    # for tweet in user_a_tweets:
    #     embeddings.append(tweet.num_embedding)
    #     labels.append(user_a.screen_name)

    # for tweet in user_b_tweets:
    #     embeddings.append(tweet.num_embedding)
    #     labels.append(user_b.screen_name)

    # comprehension
    embeddings = [tweet.num_embedding for tweet in user_a_tweets] + \
        [tweet.num_embedding for tweet in user_b_tweets]

    labels = [user_a.screen_name for tweet in user_a_tweets] + \
        [user_b.screen_name for tweet in user_b_tweets]

    # classifier.fit(embeddings, labels)
    # close to training the model. but the format might be wrong for sklearn

    print("-----------------")
    print("TRAINING THE MODEL...")

    classifier.fit(embeddings, labels)

    print("-----------------")
    print("MAKING A PREDICTION...")

    # example_embed_a = user_a_tweets[0].num_embedding
    # example_embed_b = user_b_tweets[0].num_embedding

    # prediction01 = classifier.predict([example_embed_a, example_embed_b])

    # print(prediction01)
    # take the basilica object and embed the tweet.text
    # Then put that through the classifier.
    twetext_embedding = basilica_api_client.embed_sentence(
        tweet_text, model="twitter")
    prediction02 = classifier.predict([twetext_embedding, ])

    print(prediction02[0])  # we'll pass this to the screen_name most likely

    breakpoint()

    # TODO

    return render_template("prediction_results.html",
                           screen_name_a=screen_name_a,
                           screen_name_b=screen_name_b,
                           tweet_text=tweet_text,
                           screen_name_most_likely="TODO"
                           )
