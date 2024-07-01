from flask import Flask, request  # type: ignore

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/stores")
def get_stores():
    return stores


@app.post('/store')
def create_store():
    body = request.get_json()
    new_store = {"name": body["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    body = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": body["name"], "price": body["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404
