import os
from tkinter.messagebox import showinfo
import threading 
import time

try:
    import psutil
except ImportError:
    os.system("pip install psutil")
    import psutil

def main_proc(messageB,block,spy_int):
    def show_message():
        showinfo(message="blocked", title="not today")

    while True:
        for proc in psutil.process_iter(["name"]):
            try: 
                if proc.info["name"] in block:
                    proc.kill()
                    if messageB == 1:
                        threading.Thread(target=show_message).start()
                    time.sleep(0.5)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
