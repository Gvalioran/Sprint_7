import json

import requests
import random
import string

from data import Url, DataTest


def register_new_courier_and_return_login_password():
    login_pass = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Url.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass = {
            "login": login,
            "password": password,
            "firstName": first_name,
            "status_code": response.status_code,
            "json": response.json()
        }

    return login_pass


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def login_courier(login, password):
    payload = {
        "login": login,
        "password": password,
    }
    response = requests.post(Url.LOGIN, data=payload)
    return response


def delite_courier(id_courier):
    response = requests.delete(f"{Url.DELITE_COURIER}{id_courier}")
    return response.json()


def create_order(color):
    DataTest.DATA_FOR_ORDER["color"] = color
    payload = DataTest.DATA_FOR_ORDER
    response = requests.post(Url.ORDERS, data=json.dumps(payload))
    return response.json()


def get_order_list():
    response = requests.get(Url.ORDERS)
    return response.json()
