import os
import time
import datetime
import pyautogui
import webbrowser

# path to zoom.exe
PATH = r"C:\Users\NikOne\AppData\Roaming\Zoom\bin\Zoom.exe"
ENTER_CONF_PHOTO = r"enter_the_conference.png"
ENTER_PHOTO = r"enter.png"
pyautogui.PAUSE = 0.5

''' 
    enter links or id and passwords like this: 
    [["connect_link", "year-month-day-hours-minutes"], ["connect_id", "password", "year-month-day-hours-minutes"]]
    example: [[r"https://zoom.com/1073729/", "2021-08-15-19-30"], ["2s5e8x25s", "52247167", "2021-08-15-19-30"]]
'''
conferences = []


def enter_the_conference(conf_id, conf_pass):
    if not conf_id.startswith("https"):
        pos = pyautogui.locateOnScreen(ENTER_CONF_PHOTO)
        x = pos[0] + pos[2] / 2
        y = pos[1] + pos[3] / 2
        pyautogui.click(x=x, y=y, button='left')
        time.sleep(3)
        pyautogui.typewrite(conf_id)
        pos = pyautogui.locateOnScreen(ENTER_PHOTO)
        x = pos[0] + pos[2] / 2
        y = pos[1] + pos[3] / 2
        pyautogui.click(x=x, y=y, button='left')
        time.sleep(1)
        pyautogui.typewrite(conf_pass)
        pos = pyautogui.locateOnScreen(ENTER_PHOTO)
        x = pos[0] + pos[2] / 2
        y = pos[1] + pos[3] / 2
        pyautogui.click(x=x, y=y, button='left')
    else:
        webbrowser.open(conference[0])


if __name__ == "__main__":
    def sort_by_date(conf):
        if conf[0].startswith("https"):
            date = conf[1]
        else:
            date = conf[2]
        year, month, day, hour, minute = date.split("-")
        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)).timestamp()

    conferences.sort(key=sort_by_date)

    for conference in conferences:
        if conference[0].startswith("https"):
            _date = conference[1]
        else:
            _date = conference[2]
        _year, _month, _day, _hour, _minute = _date.split("-")
        time_delta = datetime.datetime(int(_year), int(_month), int(_day), int(_hour), int(_minute)).timestamp() - \
            datetime.datetime.today().timestamp()
        if time_delta > 0:
            print("Sleeping for " + str(time_delta) + "sec")
            time.sleep(time_delta)
        else:
            continue
        os.system(r"taskkill /f /im Zoom.exe")
        os.startfile(PATH)
        time.sleep(8)
        enter_the_conference(conference[0], conference[1])
