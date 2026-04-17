#process blocker
#author: ogrizok1

from os import system
from tkinter import messagebox
import time
import threading

try:
    import psutil
except ImportError:
    system("pip install psutil")
    import psutil


def proc_stop(processes):
    print("---------------------")
    print("programm started")
    print("---------------------")
    while True:
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] in processes:
                proc.kill()

                print(time.strftime('%d.%m.%Y %H:%M:%S'))
                print(f'detected "{proc.info["name"]}"')
                print("shutdown process")
                print("---------------------")

                def message():
                    messagebox.showerror("err", "not today")
                threading.Thread(target=message).start()

#Add name of the process here to block it.
processes = ["ULTRAKILL.exe"]

proc_stop(processes)