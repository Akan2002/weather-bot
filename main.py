import requests
from config import *
from datetime import datetime
from pprint import pprint


def get_weather(city):
    try:
        responce = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")

        data = responce.json()
        sity = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timesmp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timesmp = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_timesmp - sunrise_timesmp

        return f"""
        Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Погода в городе: {sity}
        Температура: {cur_weather}
        Влажность: {humidity}
        Давление: {pressure}
        Скорость ветра: {wind}
        Восход: {sunrise_timesmp}
        Закат: {sunset_timesmp}
        Продолжительность дня: {length_of_the_day}
        """
    except Exception as ex:
        return 'Введите корректный город'