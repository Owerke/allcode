from ast import Delete
from bottle import post, request, redirect
import g
import uuid
##############################
# @post("/tweets") #this is where to posting take place
# def _():
#    tweet_title = request.forms.get("tweet_title")
#    tweet_text = request.forms.get("tweet_text")
#    tweet = {"tweet_title": tweet_title, "tweet_text":tweet_text}
#    g.TWEETS.append(tweet)
#    return redirect(f"/tweets_posted?tweet-title={tweet_title}&tweet-text={tweet_text}")#dict(tweets=g.TWEETS)


##############################
@post("/tweets")
def _():
    tweet_title = request.forms.get("tweet_title")
    tweet_text = request.forms.get("tweet_text")
    new_tweet = {
        "id":  str(uuid.uuid4()),
        "tweet_title": tweet_title,
        "tweet_text": tweet_text
    }

    g.TWEETS.append(new_tweet)

    return redirect("/tweets")
