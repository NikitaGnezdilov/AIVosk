import os
import webbrowser
import sys
import subprocess
import pyttsx3

engine = pyttsx3.init()
voices = engine.setProperty('rate', 180)

def speaker(text):
    engine.say(text)
    engine.runAndWait()

def new_year():
    webbrowser.open('https//allcalc.ru/node/1868', new=2)

def news():
    webbrowser.open('https://tengrinews.kz/', new=2)

def locationRestaurant():
    webbrowser.open('https://yandex.ru/maps/213/moscow/?ll=37.709160%2C55.687260&z=10.48',new=2)

def pizza_recipe():
    webbrowser.open("https://www.russianfood.com/recipes/bytype/?fid=30", new=2)

def cs_game():
    subprocess.Popen("C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64\cs2.exe")

def offpc():
    os.system("shutdown")

def online_map():
    webbrowser.open('https://yandex.ru/maps/200164/mir/sputnik/?ll=25.939165%2C53.170240&z=16',new=2)

def weather():
    webbrowser.open('https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE2NzJqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8', new=2)

def offBot():
    sys.exit()

def passive():
    pass