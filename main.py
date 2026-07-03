import calendar, ctypes, json
from PIL import Image, ImageDraw
from screeninfo import get_monitors
import platform
from types import SimpleNamespace

congif ={"hi":"hi"}
import json

with open('congif.congif', 'r', encoding='utf-8') as file:
    data = json.load(file)
    congif =(SimpleNamespace(**data))
    file.close

if platform.system() == "Windows":
    import ctypes
    width = ctypes.windll.user32.GetSystemMetrics(0)
    heigth ,width = None
else:
    # Linux/macOS code here
    # print(get_monitors()[0].width)
    width = get_monitors()[0].width
    heigth = get_monitors()[0].height


def makeImg():
    background = Image.new("RGB",(width,heigth),"black")
    img = Image.new("RGBA",(width,heigth),(0,0,0,0))
    draw = ImageDraw.Draw(img)
    

