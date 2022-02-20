from bottle import get, view
import g
##############################
@get("/tweets")
@view("tweets")
def _():
    return dict(tweets=g.TWEETS)
