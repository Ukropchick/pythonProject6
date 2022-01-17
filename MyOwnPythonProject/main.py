from pyowm import *


def weather_report():
    city = input("Введите название города: ")
    own = OWM('ecc37d11852cb8b06c7f97ee0a1bb259')
    mgr = own.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    return w


print(weather_report())

'''Это тест'''