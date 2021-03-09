# TODO: 현재 날씨 요청과 일기예보 요청 

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


def generateRequest(region='Anyang-si,KR'):
    query['q'] = region
    res = requests.request("GET", url, params=query)
    respond = json.loads(res.text)

    if str(res.status_code).startswith("4"):
        raise APIRequestError(f"{res.status_code} {respond['message']}")

    return res.status_code, respond


def getAPIKey():
    return APIKEY


if __name__ == '__main__':
    from pprint import pprint
    pprint(generateRequest())
