from tools import detector


def test_get_friends(monkeypatch):
    def mock_get_friends(user):
        return [
            {
                "x_info": "appType=1&curr=rub&dest=-1257786&regions=80,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&spp=0",
                "latitude": 55.753737,
                "address": "Москва",
                "id": 1,
                "longitude": 37.6201,
            },
            {
                "x_info": "appType=1&curr=rub&dest=-3398094&regions=80,38,4,64,83,33,68,70,69,30,86,40,1,66,110,22,31,48,114&spp=0",
                "latitude": 54.901883469,
                "address": "г. Альметьевск (Республика Татарстан), улица Тимирязева, д. 15",
                "id": 4,
                "longitude": 52.308762677,
            },
        ]

    monkeypatch.setattr(detector, "send_request", mock_get_friends)

    assert len(detector.send_request("testdrivenio")) == 2
