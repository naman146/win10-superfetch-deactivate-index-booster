"""Please provide admin rights for the program to run freely"""

import os , fnmatch , path
import win32serviceutil
import subprocess
global result,sortedlist,val
result=[]
sortedlist=[]
val = ""
#creating list of service
service_name= ['SysMain']

#For starting the service
def servStart():
    msg = []
    for service in service_name:
        if win32serviceutil.QueryServiceStatus(service)[1] == 1:
            try:
                win32serviceutil.StartService(service)
                msg.append(("Service " + service + " is started"))
            except:
                msg.append(("Service " + service + " has an error"))
        else:
            msg.append(("Service %s is already running" %service))
    return msg

#For Stopping the service        
def servStop():
    msg = []
    for service in service_name:
        if 1 < win32serviceutil.QueryServiceStatus(service)[1] <= 4:
            try:
                win32serviceutil.StopService(service)
                msg.append(("Service " + service + " is stopped"))
            except:
                msg.append(("Service " + service + " has an error"))
        else:
            msg.append(("Service %s is not running" %service))
    return msg

"""def servStatus():
    for service in service_name:
        if win32serviceutil.QueryServiceStatus(service)[1] == 4:
            servStart(service)
        elif win32serviceutil.QueryServiceStatus(service)[1] == 1:
            servStop(service)
        else:
            print("Service %s is in unknown state" %service)"""
            
def driveFetch():
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s' % d for d in dl if os.path.exists('%s:' % d)]
    return drives


def searchSplitter(searchlist):
    global sortedlist
    searchlist = [b[::-1] for b in searchlist]
    searchlist=[b.split("\\",1) for b in searchlist]
    sortedlist=[]
    for b in searchlist:
        sortedlist.append(b[0])
    sortedlist=[b[::-1] for b in sortedlist]
    return sortedlist


def search(pattern , dirpath):
    global result
    result=[]
    for root, dirs, files in os.walk(dirpath):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return searchSplitter(result)

def selectedValue(value):
    global val
    val = value
    return openFile(val,result,sortedlist)
    

def openExplorer(filepath):
    filepath = "explorer " + filepath
    print(filepath)
    subprocess.call(filepath, shell=True)


def openFile(selectedvalue,result,sortedlist):
    for file in sortedlist:
        if selectedvalue in file:
            ind = sortedlist.index(file)
            print(result[ind])
            return openExplorer(result[ind])



