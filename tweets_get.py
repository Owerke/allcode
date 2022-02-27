from bottle import get, view, response, request, redirect
import g
##############################


@get("/tweets")
@view("tweets")
def _():
    response.set_header("Cache-Control", "no-cahce, no-store, must-revaildate")
    response.add_header("Pragma", "no-cache")
    # from the cookie we extract the user session id
    user_session_id = request.get_cookie("user_session_id")
    if not user_session_id:
        return redirect("/login")
    if user_session_id not in g.sessions:
        return redirect("/login")
    user = g.sessions[user_session_id]
    # if the user session id is not there, we redirect the user to the login
    if (user_session_id not in g.sessions):
        return redirect("/index")
    return dict(tweets=g.TWEETS)
