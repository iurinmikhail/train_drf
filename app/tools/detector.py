# функция отправки запросов на сервер
import requests


def send_request(url):
    response = requests.get(url)
    return response


if __name__ == "__main__":
    url = "http://127.0.0.1:8080/pick_up"
    resp = send_request(url)
    print(resp.text)
