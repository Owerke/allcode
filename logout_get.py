
from bottle import get, view, request, redirect, response, post
import g
@get("/logout")
@view("logout")
def _():
    user_session_id = request.get_cookie("user_session_id") #extract the user session id from cookie
    g.sessions.pop(user_session_id) #removing it from the session dictionary
    response.set_cookie("user_session_id", "", expires=0)
    print("#"*30)
    print("logout")
    print(user_session_id)
    print(g.sessions)
    return redirect("/index")
