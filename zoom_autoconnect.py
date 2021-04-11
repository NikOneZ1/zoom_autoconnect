import os
import time
import datetime
import webbrowser
import tkinter as tk

PATH = r"C:\Users\NikOne\AppData\Roaming\Zoom\bin\Zoom.exe"

window = tk.Tk()

window.rowconfigure(5, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

conf_fields = {}
conferences = []
number = [0]


# adding conference fields to the application window
def add_conference():
    number[0] += 1
    conf_fields[number[0]] = []
    link = tk.Entry(master=window)
    link.grid(row=number[0], column=0, sticky="nsew")
    conf_fields[number[0]].append(link)
    _time = tk.Entry(master=window)
    _time.grid(row=number[0], column=1)
    conf_fields[number[0]].append(time)


# entering conference
def enter_conf(link, path):
    os.system(r"taskkill /f /im Zoom.exe")
    os.startfile(path)
    time.sleep(8)
    webbrowser.open(link)


# start application
def start():
    if start_btn["text"] == "Start":
        start_btn["text"] = "Stop"
        for fields in conf_fields:
            conferences.append([conf_fields[fields][0].get(), conf_fields[fields][1].get()])

        # sort conferences by date
        def sort_by_date(conf):
            if conf[0].startswith("http") or conf[0].startswith("www"):
                date = conf[1]
            else:
                date = conf[2]
            year, month, day, hour, minute = date.split("-")
            return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)).timestamp()

        conferences.sort(key=sort_by_date)

        for conference in conferences:
            if conference[0].startswith("http") or conference[0].startswith("www"):
                _date = conference[1]
            else:
                _date = conference[2]
            _year, _month, _day, _hour, _minute = _date.split("-")
            time_delta = datetime.datetime(int(_year), int(_month), int(_day), int(_hour), int(_minute)).timestamp() - \
                         datetime.datetime.today().timestamp()
            if time_delta > 0:
                print("Sleeping for " + str(time_delta) + "sec")
                # time.sleep(time_delta)
                window.after(int(time_delta * 1000), enter_conf, conference[0], PATH)
            else:
                continue

    else:
        exit()


start_btn = tk.Button(master=window, text="Start", command=start)
start_btn.grid(row=0, column=0, sticky="nsew")

btn_add = tk.Button(master=window, text="Add conference", command=add_conference)
btn_add.grid(row=0, column=1, sticky="nsew")

window.mainloop()
