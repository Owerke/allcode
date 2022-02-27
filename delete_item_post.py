from bottle import post, redirect, request
import g

##############################


@post("/delete-tweet")
def _():
    # VALIDATE
    tweet_id = request.forms.get("tweet-id")
    # Delete the item for if enumarate
    for index, tweet in enumerate(g.TWEETS):
        if tweet["id"] == tweet_id:
            g.TWEETS.pop(index)
            return redirect("/tweets")

    return redirect("/tweets")


@post("/update_tweet")
def update_tweet():
    tweet_id = request.forms.get("tweet-id")
    tweet_button_action = request.forms['submit']

    if tweet_button_action == "delete":
        tweet_id = request.forms.get("tweet-id")
        for index, tweet in enumerate(g.TWEETS):
            if tweet["id"] == tweet_id:
                g.TWEETS.pop(index)
                return redirect("/tweets")

    elif tweet_button_action == "update":
        for index, tweet in enumerate(g.TWEETS):
            if tweet["id"] == tweet_id:
                tweet_title = request.forms.get("tweet_title")
                tweet_text = request.forms.get("tweet_text")
                g.TWEETS[index]["tweet_title"] = tweet_title
                g.TWEETS[index]["tweet_text"] = tweet_text
                return redirect("/tweets")

                # uj html oldalat csinálni ahol uj post tweet legyen amivel be utok irni uj erteket neki.
