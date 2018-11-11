import win32evtlog
import win32api
import win32con
import win32security
import win32evtlogutil
import time
import servicemanager
import sys
import win32serviceutil
from SMWinservice import SMWinservice

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
            logType = "Application"
            ph = win32api.GetCurrentProcess()
            th = win32security.OpenProcessToken(ph, win32con.TOKEN_READ)
            my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]

            win32evtlogutil.ReportEvent(logType, 2,
                                        strings=["The message text for event 2", "Another insert"],
                                        data="Raw\0Data".encode("ascii"), sid=my_sid)
            time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonCornerExample)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PythonCornerExample)