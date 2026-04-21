import os
from tkinter.messagebox import showinfo
from tkinter import *
import threading 
import time

try:
    import psutil
except ImportError:
    os.system("pip install psutil")
    import psutil

def show_message():
    showinfo(message="blocked", title="not today")

def proc_stop(block):
    while True:
        for proc in psutil.process_iter(["name"]):
            try: 
                if proc.info["name"] in block:
                    proc.kill()
                    if messageB.get() == 1:
                        threading.Thread(target=show_message).start()
                    time.sleep(0.5)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

def enter_btn():
    blocked.append(proc_entry.get())

def turn_on():
    root.destroy()
    proc_stop(blocked)

processes = []
blocked = []
sys_proc = [
            "svchost.exe","csrss.exe","System","",
            "wininit.exe","smss.exe","services.exe","winlogon.exe",
            "LsaIso.exe","lsass.exe","fontdrvhost.exe","smartscreen.exe",
            "dwm.exe","msedge.exe","CefSharp.BrowserSubprocess.exe",
            "SystemSettings.exe","NVDisplay.Container.exe","NVIDIA Overlay.exe",
            "MemCompression","conhost.exe","spoolsv.exe","armsvc.exe",
            "nvcontainer.exe","jhi_service.exe","WMIRegistrationService.exe",
            "nvWmi64.exe","MpDefenderCoreService.exe","wslservice.exe",
            "service_update.exe","powershell.exe","MsMpEng.exe","WmiPrvSE.exe",
            "backgroundTaskHost.exe","msedgewebview2.exe","ApplicationFrameHost.exe",
            "gamingservicesnet.exe","sihost.exe","wlanext.exe","taskhostw.exe",
            "NgcIso.exe","nvsphelper64.exe","AggregatorHost.exe","explorer.exe",
            "ShellHost.exe","CrossDeviceResume.exe","SecurityHealthService.exe",
            "SearchIndexer.exe","RuntimeBroker.exe","SearchHost.exe","WidgetService.exe",
            "StartMenuExperienceHost.exe","PhoneExperienceHost.exe","LockApp.exe",
            "ctfmon.exe","NisSrv.exe","crashhelper.exe","TextInputHost.exe",
            "CrossDeviceService.exe","ms-teams.exe","UserOOBEBroker.exe","jusched.exe",
            "XboxPcAppFT.exe","SearchProtocolHost.exe","System Idle Process"
            ]

root = Tk()
root.title("process blocker")
root.geometry("600x500+1000+400")
root.resizable(False,False)

for proc in psutil.process_iter(["name"]):
    #checks if the process is in the filter or has already been added to the list
    if proc.info["name"] not in sys_proc and proc.info["name"] not in processes:
        processes.append(proc.info["name"])

processes_var = Variable(value=processes)
proc_list = Listbox(listvariable=processes_var,font=("Arial",12))
proc_list.pack(side=LEFT,fill=Y,padx=20,pady=10)

first_label = Label(text="Insert here the name of the process you want to block.",font=("Arial",12))
first_label.pack(anchor="nw",pady=10)

proc_entry = Entry(font=("Arial",12),width=40)
proc_entry.pack(anchor="nw",pady=10)

enter_button = Button(command=enter_btn,text="Enter",width=20,font=("Arial",12))
enter_button.pack(anchor="nw",pady=10)

messageB  = IntVar()
message_check = Checkbutton(text="use messagebox",variable=messageB)
message_check.pack(anchor="nw",pady=10)

start_btn = Button(text="turn on", command=turn_on)
start_btn.pack(anchor="nw",pady=10)

root.mainloop()

