import requests
import json

URL = "http://127.0.0.1:8000/studentapi/2/"


def show_data(id=None):
    data = {
        "id": id
    }
    json_data = json.dumps(data)
    response = requests.get(url=URL, data=json_data)
    print(response.json())


show_data(2)


def create_data():
    data = {
        "roll": 102,
        "name": "Yashraj"
    }
    json_data = json.dumps(data)

    response = requests.post(url=URL, data=json_data)
    print(response.json())


# create_data()

def update_data():
    data = {
        'id': 2,
        "roll": 103,
        "name": "raj"
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    print(response.json())


# update_data()


def delete_data():
    data = {
        'id': 1
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    print(response.json())


# delete_data()
