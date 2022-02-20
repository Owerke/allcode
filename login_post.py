from bottle import post, request, redirect, response
import uuid
import g
import re



##############################
@post("/login") #this is where to login take place
def _():
    # VALIDATE
# FIRST THING: Always check if the vriable was passed in the form
    if not request.forms.get("user_email"):
        return redirect("/login?error=user_email")    
    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email")

# FIRST THING: Always check if the vriable was passed in the form
    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) < 6:
        return redirect(f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) > 50:
        return redirect(f"/login?error=user_password&user_email={user_email}")
    
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
