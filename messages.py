from datetime import datetime


def prepare_weather_message(weather_json: dict) -> str:
    sunset_time = datetime.fromtimestamp(weather_json["sys"]["sunset"])
    current_time = datetime.now()
    if sunset_time > current_time:
        delta_seconds = (sunset_time - current_time).seconds
        hours_to_sunset = delta_seconds // 3600
        minutes_to_sunset = round(delta_seconds % 3600 / 60)
        sun_state_message = f"🌚 Сонечка не буде через {hours_to_sunset}:{minutes_to_sunset} годин"
    else:
        sun_state_message = "🌚 Сонечко заховалось від очей"

    wind_speed = round(weather_json["wind"]["speed"] * 1.609344, 2)
    temp_feels_like = weather_json["main"]["feels_like"]
    humidity = weather_json["main"]["humidity"]

    template = f"""Стан погоди на {current_time.strftime("%Y-%m-%d %H:%M:%S")}:
    
    {sun_state_message}
    🌬 Вітерець має швидкість {wind_speed} м/c
    🐝 Жужа відчуває температуру {temp_feels_like}°C і вологість {humidity}%
    """

    return template


if __name__ == '__main__':
    test_json = {
        'base': 'stations',
        'clouds': {'all': 19},
        'cod': 200,
        'coord': {'lat': 48.67, 'lon': 26.62},
        'dt': 1593772781,
        'id': 686949,
        'main': {'feels_like': 29.26,
              'humidity': 64,
              'pressure': 1008,
              'temp': 27.22,
              'temp_max': 27.22,
              'temp_min': 27.22},
        'name': 'Zinkivtsi',
        'sys': {'country': 'UA',
             'id': 2003483,
             'sunrise': 1593742581,
             'sunset': 1593800334,
             'type': 3},
        'timezone': 10800,
        'weather': [{'description': 'few clouds',
                  'icon': '02d',
                  'id': 801,
                  'main': 'Clouds'}],
        'wind': {'deg': 283, 'gust': 4.47, 'speed': 2.24}
    }
    print(prepare_weather_message(test_json))