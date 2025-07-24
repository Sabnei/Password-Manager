import json
import os

FILE_PATH = "storage.json"


def load_data():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def add_password(service, username, password):
    data = load_data()
    data[service] = {"username": username, "password": password}
    save_data(data)


def get_password(service):
    return load_data().get(service)


def list_services():
    return list(load_data().keys())


def delete_password(service):
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        return True
    return False
