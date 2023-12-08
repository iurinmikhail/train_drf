# функция отправки запросов на сервер
import requests

class Detector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def send_request(self, url):
        response = requests.get(url)
        return response



if __name__ == "__main__":
    url = "http://127.0.0.1:8080/pick_up"
    resp = Detector(x=None, y=None).send_request(url)
    print(resp.text)
