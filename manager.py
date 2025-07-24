import json
import os
from crypto_utils import load_encrypted, save_encrypted

FILE_PATH = "storage.json"


def load_data(key):
    # if not os.path.exists(FILE_PATH):
    #     return {}
    # with open(FILE_PATH, "r") as file:
    #     try:
    #         return json.load(file)
    #     except json.JSONDecodeError:
    #         return {}
    return load_encrypted(key)


def save_data(data, key):
    save_encrypted(data, key)


def add_password(service, username, password, key):
    data = load_data(key)
    data[service] = {"username": username, "password": password}
    save_data(data, key)


def get_password(service, key):
    return load_data(key).get(service)


def list_services(key):
    return list(load_data(key).keys())


def delete_password(service, key):
    data = load_data(key)
    if service in data:
        del data[service]
        save_data(data, key)
        return True
    return False
