from bottle import get, view, response, request, redirect
import g
##############################
@get("/admin")
@view("admin")
def _():
    response.set_header("Cache-Control", "no-cahce, no-store, must-revaildate")
    response.add_header("Pragma", "no-cache")
    user_session_id = request.get_cookie("user_session_id")  # from the cookie we extract the user session id
    print("#"*30)
    print("admin")
    print(user_session_id)
    if not user_session_id:
        return redirect("/login")
    if user_session_id not in g.sessions:
        return redirect("/login")
    user = g.sessions[user_session_id]
    if (user_session_id not in g.sessions):  # if the user session id is not there, we redirect the user to the login
        return redirect("/index")
    user = g.sessions[user_session_id] #extract the user, from the session
    return dict(user=user)  # return the user to the view.
