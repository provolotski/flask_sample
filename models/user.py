import requests
from flask_login import UserMixin
import os
from dotenv import load_dotenv

load_dotenv()


def authenticate(username, password, domain):
    url = f'http://{os.getenv("AUTH_URL")}:{os.getenv("AUTH_PORT")}/api/v1/auth/login'
    payload = {'username': username, 'password': password, 'domain': domain}
    print(payload)
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        user = User(-1, username, r.json()['access_token'], r.json()['refresh_token'])

        return user
    else:
        return None


class User(UserMixin):
    def __init__(self, id, username, access_token, refresh_token):
        self.id = id
        self.username = username
        self.access_token = access_token
        self.refresh_token = refresh_token

    @staticmethod
    def get_def_user(user_id):
        return User(user_id, 'test', 'asd', 'asd')
