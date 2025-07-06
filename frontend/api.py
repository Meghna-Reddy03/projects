import requests


def login(username, password):
    url = f"http://127.0.0.1:8000/create?name={username}&password={password}"
    res = requests.post(url)
    if res.status_code == 200:
        return res.json()