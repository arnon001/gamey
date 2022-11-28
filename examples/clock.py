import datetime, time
from gamey import *

screen = Screen(width=500,height=200)
date_text = None

def create_date():
    global date_text
    now_date = datetime.datetime.now()
    date = f"Date: {str(now_date.year)}/{str(now_date.month)}/{str(now_date.day)}"
    date_text = Text(x=480/2, y=10, bg_color=None, text=date)

create_date()

while True:
    now_time = time.localtime()

    time_txt = Text(x=screen.width/2, y=100, bg_color=None, text=str(f"{now_time[3]}:{now_time[4]}:{now_time[5]}"), font_size=100)

    screen.bg_color(75, 105, 255)

    time_txt.draw()
    date_text.draw()

    if now_time[3] == 23 or now_time[3] == 00:
        create_date()

    main_loop()