import json
import requests

URL = "http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data ={}
    if data is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    try:
        data = r.json()
        print(data)
    except:
        # pass
        print("Error from server: " + str(r.content))
    # data = r.json()
    # print()

# get_data(1)


def post_data():
    data ={
        "name":"vivek",
        'roll':7,
        'city':'bhilwara'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    try:
        dat = r.json()
        print(dat)
    except:
        print(str(r.content))

# post_data()


def update_data():
    data = {
        "id":1,
        "name":"rahul",
        'city':'bihar'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    try:
        dat = r.json()
        print(dat)
    except:
        print(str(r.content))

# update_data()


def delete_data():
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    print(r.json())


delete_data()



