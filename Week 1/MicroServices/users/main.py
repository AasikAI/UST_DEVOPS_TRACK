from fastapi import FastAPI

app = FastAPI()
user_data = ["user 1", "user 2"]
app.route("/users")
def get_users():
    return user_data

