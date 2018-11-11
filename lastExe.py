from datetime import datetime

'''
Created by Kal Chokanov
Data Structure for paths to executables and their latest launch time
'''

class lastExe:
    def __init__(self, path):
            self.path = path
            self.checked = False
            self.lastLaunch = datetime.fromordinal(1)
    def toString(self):
            return "Exe: " + self.path + ", Last launched: " + str(self.lastLaunch)

def genlist(pathList):
    arr = []
    for i in range(len(pathList)):
        arr.append(lastExe(pathList[i]))
    return arr

def test():
    t = lastExe("python.exe")
    print(t.toString())

if __name__ == '__main__':
    test()
