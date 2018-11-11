import win32api
import time
import servicemanager
import sys
import win32serviceutil
from datetime import datetime
from SMWinservice import SMWinservice
from checkLog import getLastExecuted
from lastExe import genlist

class PythonCornerExample(SMWinservice):
    _svc_name_ = "MegyKod"
    _svc_display_name_ = "MegyKod"
    _svc_description_ = "Have you been a good programmer?"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            with open('D:\Docs\Code\Python\MegyKod\Paths', 'r') as pool:    #replace with file containing paths to IDE executables
                paths = pool.readlines()
            pathlist = genlist(paths)
            pathlist = getLastExecuted(None, pathlist)
            do = False
            for item in pathlist:
                if ((datetime.now() - item.lastLaunch).days > 0):
                    do = not do
            if do:
                win32api.MessageBox(0, 'You haven\'t written code in 24 hours Kal!', 'MegyKod', 0x00001000)
            time.sleep(86400)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonCornerExample)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PythonCornerExample)