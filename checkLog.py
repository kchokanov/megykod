import win32evtlog
import win32api
import win32evtlogutil
from lastExe import lastExe

'''
Written by Kal Chokanov
Modified from demo code @ *python install folder*\Lib\site-packages\win32\Demos\eventLogDemo.py
'''


def getLastExecuted(computer, exeList):
    logType = "Security"
    query = "A new process has been created."
    eventLog = win32evtlog.OpenEventLog(computer, logType)  # Object consisting of all records in requested log

    while True:
        # Magic code BEGINS
        objects = win32evtlog.ReadEventLog(eventLog, win32evtlog.EVENTLOG_BACKWARDS_READ |
                                           win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
        if not objects:
            break
        # Magic code ENDS
        for object in objects:
            # get it for testing purposes, but don't print it. - Not written by me. No idea what this does
            record = win32evtlogutil.SafeFormatMessage(object, logType)
            try:
                recordLines = record.splitlines()
                if recordLines[0] == query:
                    for i in range(len(recordLines)):
                        if "New Process Name:" in recordLines[i]:
                            for j in range(len(exeList)):
                                if exeList[j].path in recordLines[i]:
                                    if not exeList[j].checked:  # record list is sorted newest to oldest, so we check to see if the processes last launch time has already been recorded
                                        exeList[j].checked = True
                                        exeList[j].lastLaunch = object.TimeGenerated.Format()   # returns a String of the timestamp of the record
                                    break
                            break

            except UnicodeError:
                print("(unicode error printing message: repr() follows...)")
                print(repr(record))

    win32evtlog.CloseEventLog(eventLog)
    return exeList


def test():
    # check if running on Windows NT, if not, display notice and terminate
    if win32api.GetVersion() & 0x80000000:
        print("This sample only runs on NT")
        return

    exelist = []
    exelist.append(lastExe('python.exe'))
    exelist.append(lastExe('conhost.exe'))
    computer = None     # None refers back to localhost
    exelist = getLastExecuted(computer, exelist)
    for exe in exelist:
        print(exe.toString())


if __name__ == '__main__':
    test()
