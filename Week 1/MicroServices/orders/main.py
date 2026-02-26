from fastapi import FastAPI

app = FastAPI()
order_data = ["Iphone", "Asus-Rog"]
app.route("/orders")
def get_users():
    return order_data


