from bottle import get, view, request, redirect
import g
@get("/logout")
@view("logout")
def _():
    user_session_id = request.get_cookie("user_session_id") #extract the user session id from cookie
    g.sessions.pop(user_session_id) #removing it from the session dictionary
    return redirect("/index")