user=set()
def login_user(u_id):
    user.add(u_id)
login_user("u1")
login_user("u2")
login_user("u1")
login_user("u3")
print(len(user))
