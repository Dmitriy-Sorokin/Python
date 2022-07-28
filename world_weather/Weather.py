import time
from tkinter import messagebox
from tkinter import ttk

import requests
from ttkthemes import ThemedTk

API_KEY = '5e1ce895b1f7950c8267adecc8ce4989'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'


# https://api.openweathermap.org/data/2.5/weather?appid=key&q=minsk,by


def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
        sunset = time.strftime('%H:%M:%S', sunset_struct_time)
        return f'Место положение: {city}, {country} \nТемпература: {temp} °С \АТМ. давление: {press} гПА \nВлажность: {humidity}% \nСкорость ветра: {wind} м/с ' \
               f'\nПогодные условия: {desc} \nВосход: {sunrise} \nЗакат {sunset}'
    except:
        return "Ошибка получения данных..."


def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning('Warning', 'Введите запрос в формате city, country_code')
    else:
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric',
            'lang': 'ru'
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label['text'] = print_weather(weather)


root = ThemedTk(theme='arc')
root.geometry('500x400+1000+300')
root.resizable(False, False)

s = ttk.Style()
s.configure('TLabel', padding=5, font='Arial 11')

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relheight=1, relwidth=0.7)

button = ttk.Button(top_frame, text='get weather', command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor='nw')
label.place(relheight=1, relwidth=1)

entry.bind('<Return>', get_weather)

root.mainloop()
