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

#You can change this filter.
sys_proc = [
            "svchost.exe","csrss.exe",
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
            "XboxPcAppFT.exe","SearchProtocolHost.exe"
            ]

processes = []
blocked = []

for proc in psutil.process_iter(["name"]):
    #checks if the process is in the filter or has already been added to the list
    if proc.info["name"] not in sys_proc and proc.info["name"] not in processes:
        processes.append(proc.info["name"])
        print(proc.info["name"])

print("---------------------")
print("Write which processes you want to block. When finished, write 0.")
n = input()
while n != "0":
    blocked.append(n)
    n = input()

proc_stop(blocked)