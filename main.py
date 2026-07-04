import calendar, ctypes, json , math
from PIL import Image, ImageDraw
from screeninfo import get_monitors
import platform ,os
from types import SimpleNamespace
from datetime import datetime ,date
from subprocess import run

with open('config.config', 'r', encoding='utf-8') as file:
    data = json.load(file)
    config =(SimpleNamespace(**data))
    file.close
print(config)

year = datetime.now().year
weeks = date(year, 12, 28).isocalendar()[1]
fileName = config.fileName
path = "/home/hexene/Pictures"
wallpaperPath = os.path.join(path,fileName)
firstDay = date(year, 1, 1).weekday()
lastDay = date(year, 12, 31).weekday()
today = date.today().weekday()
weeks_passed = (date.today().timetuple().tm_yday - 1) // 7
# print(today,weeks_passed)


congif ={"hi":"hi"}
import json


if platform.system() == "Windows":
    import ctypes
    width = ctypes.windll.user32.GetSystemMetrics(0)
    heigth ,width = None
else:
    # Linux/macOS code here
    width = get_monitors()[0].width
    heigth = get_monitors()[0].height

    

def makeImg():
    background = Image.new("RGB",(width,heigth),"#FAF0FF")
    img = Image.new("RGBA",(width,heigth),(0,0,0,0))
    draw = ImageDraw.Draw(img)
    # draw.rectangle(((width/2)-widthx/2,(heigth/2)-heighty/2,(width/2)+widthx/2,(heigth/2)+heighty/2),fill=congif.color2)
    boxSize = config.scale*4
    gap = config.scale*1
    if year%4==0:
        days = 366
    else:
        days = 365

    for week in range(weeks):
        for day in range(7):
            # print(week,day,week*7 +day)
            boxHeight = (boxSize+gap)*7
            boxwidth = (boxSize+gap)*weeks
            drawCell = True
            dayPassed = False
            isToday = False
            if (week ==0 and day <=firstDay) or (week == weeks-1 and day-1 >lastDay):
                drawCell = False

            if week < weeks_passed:
                dayPassed = True
                # print(week,day,today)

            elif week == weeks_passed and day <= today:
                dayPassed = True

            if week == weeks_passed and day == today+1:
                isToday = True
            if drawCell:
                x1 = week*(boxSize+gap)+((width/2)-boxwidth/2)
                y1 = day*(boxSize+gap)+((heigth/2)-boxHeight/2)
                cords =(x1,y1,x1+boxSize,y1+boxSize)
                if dayPassed:
                    draw.rectangle(cords,fill=config.color)
                else :
                    draw.rectangle(cords,fill=config.color2)
                if isToday:
                    draw.rectangle(cords,fill=config.color3)
                    print("color3")

    background.paste(img,(0,0),img)
    background.save(f'{fileName}')

makeImg()   
run([
    "cp",fileName,wallpaperPath
])
