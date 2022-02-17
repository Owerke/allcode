from bottle import post, request, redirect, response
import uuid
import g



##############################
@post("/login") #this is where to login take place
def _():
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    for user in g.USERS:
        if user_email == user["email"] and user_password == user["password"]:
            user_session_id = str(uuid.uuid4())
            g.sessions[user_session_id] = user
            print("#"*30)
            print(g.sessions)
            response.set_cookie("user_session_id", user_session_id) #this user id session will be passed to the cookie
            return redirect ("/admin")
    return redirect ("/login")