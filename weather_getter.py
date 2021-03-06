import requests
import base64
import json

APIKEY = base64.b64decode(open("sources/apikey", 'r').read().encode()).decode()
url = "http://api.openweathermap.org/data/2.5/weather"
query = {
    "appid": APIKEY,
    'q': "Anyang-si,KR",
    'units': "metric",
    'lang': "KR"
}


class APIRequestError(Exception):
    __module__ = Exception.__module__


def generateRequest(**data):
    res = requests.request("GET", url, params=query, data=json.dumps(data))
    respond = json.loads(res.text)

    if str(res.status_code).startswith("4"):
        raise APIRequestError(f"{res.status_code} {respond['message']}")

    return res.status_code, respond


def getAPIKey():
    return APIKEY


if __name__ == '__main__':
    from pprint import pprint
    pprint(generateRequest())
