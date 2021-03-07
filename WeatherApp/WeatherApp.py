import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test(entry):
    print("This is the entry:", entry)

    # api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
    # a030c026c3c3a5ca23334603370e6722

def formatResponse(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        finalString = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        finalString = 'There was a problem retrieving the information.'

    return finalString

def getWeather(city):
    weatherKey = 'a030c026c3c3a5ca23334603370e6722'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weatherKey, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = formatResponse(weather)

root = tk.Tk() # Sets root

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH) #Creates base application
canvas.pack()

backgroundImage = tk.PhotoImage(file = 'landscape.png')
backgroundLabel = tk.Label(root, image = backgroundImage)
backgroundLabel.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = ('Courier', 18))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text="Get Weather", font = ('Courier', 12), command = lambda: getWeather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

lowerFrame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lowerFrame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lowerFrame, font = ('Courier', 18), anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth = 1, relheight = 1)

root.mainloop()