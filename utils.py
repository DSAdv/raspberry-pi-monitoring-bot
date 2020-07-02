import requests
import config

from urllib.parse import urljoin
from pprint import pprint

WEATHER_COORDINATES = {
    "latitude": "48.669722",
    "longitude": "26.619444"
}


def request_ip_information(ip_address: str):
    url = urljoin("http://api.ipstack.com", ip_address)
    json_response = requests.get(url, params={
        "access_key": config.IP_STACK_ACCESS_KEY
    }).json()
    return json_response


def request_weather_information(latitude: str, longitude: str):

    def temp_kelvin_to_celsius(value: float):
        return round(value - 273.15, 3)

    url = "http://api.openweathermap.org/data/2.5/weather"
    json_response = requests.get(url, params={
        "lat": latitude,
        "lon": longitude,
        "appid": config.OPEN_WEATHER_ACCESS_KEY
    }).json()

    for key in ["temp", "temp_min", "temp_max", "feels_like"]:
        json_response["main"][key] = temp_kelvin_to_celsius(json_response["main"][key])

    return json_response





if __name__ == '__main__':
    # pprint(request_ip_information("27.78.14.83"))
    pprint(request_weather_information(**WEATHER_COORDINATES))