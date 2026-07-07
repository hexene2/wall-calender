import calendar, ctypes, json , math
from PIL import Image, ImageDraw
from screeninfo import get_monitors
import platform ,os
from types import SimpleNamespace
from datetime import datetime ,date
from subprocess import run
from pathlib import Path
print(Path.home())   
configPath = os.path.join(Path.home(),".config","wall-calender","config.config") 
with open(configPath, 'r', encoding='utf-8') as file:
    data = json.load(file)
    config =(SimpleNamespace(**data))
    file.close
print(config)


Date = date.today()
# Date = date.today()
today = Date.weekday()
year = Date.year
weeks = date(year, 12, 28).isocalendar()[1]
firstDay = date(year, 1, 1).weekday()
lastDay = date(year, 12, 31).weekday()
weeks_passed = Date.isocalendar().week


#config paths
fileName = config.fileName 
path = config.filepath
backgroundPath = os.path.join(Path.home(),".config","wall-calender",config.backgroundPNG) 
wallpaperPath = os.path.join(path,fileName)

congif ={"hi":"hi"}


if platform.system() == "Windows":
    print("windows not supported")
    
else:
    width = get_monitors()[0].width
    heigth = get_monitors()[0].height

def makeImg():
    background =Image.open(backgroundPath)
    background = background.resize((width,heigth),Image.Resampling.LANCZOS)
    img = Image.new("RGBA",(width,heigth),(0,0,0,0))
    draw = ImageDraw.Draw(img)
    # draw.rectangle(((width/2)-widthx/2,(heigth/2)-heighty/2,(width/2)+widthx/2,(heigth/2)+heighty/2),fill=congif.color2)
    boxSize = config.scale*4
    gap = config.scale*1
    if year%4==0:
        days = 366
    else:
        days = 365
    boxHeight = (boxSize+gap)*7
    boxwidth = (boxSize+gap)*weeks
    # draw.text(())
    if config.isBlackBackground:
        draw.rectangle(((width/2)-(boxwidth/2)-gap,(heigth/2)-(boxHeight/2)-gap, (width/2)+(boxwidth/2)+gap,(heigth/2)+(boxHeight/2)+gap),fill="black")
    for week in range(weeks):
        for day in range(7):
            # print(week,day,week*7 +day)
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

            if week == weeks_passed and (day == today+1):
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
                    print("color3",x1,y1)
                

    background.paste(img,(0,0),img)
    background.save(f'{fileName}')

makeImg()
run([
    "cp",fileName,wallpaperPath
])

run([
    "rm",fileName
])
