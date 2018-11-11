import time
import ctypes
import random
from pathlib import Path
import servicemanager
import sys
import win32serviceutil
from SMWinservice import SMWinservice

class PythonCornerExample(SMWinservice):
    _svc_name_ = "Example"
    _svc_display_name_ = "Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:\\{x}.txt').touch()
            time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonCornerExample)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PythonCornerExample)