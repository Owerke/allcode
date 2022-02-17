from bottle import get, view, request

##############################
# query string expected with user-email
@get("/signup-ok") 
@view("signup-ok")
def _():
  user_email = request.params.get("user-email")
  user_name = request.params.get("user-name")
  user_lastname = request.params.get("user-lastname")
  user_password = request.params.get("user-password") #not sure about this if it is needed
  return dict(user_email=user_email, user_name=user_name, user_lastname=user_lastname, user_password=user_password)