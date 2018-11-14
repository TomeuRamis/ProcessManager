import os
import subprocess
import FileGenerator
import json


pathReq = "Files/Requests/"
pathInProg = "Files/InProgress/"
pathFinish = "Files/Finished/"

def checkForRequests(): #try
    files = os.listdir(pathReq)
    for i, file in files:
        print(files)              #log
        f = open(pathReq + files, "r")
        #Reads a string and transforms it to a Dictionary
        request = json.load(f)
        #Avaluate the type of process requested
        if request["type"] is "fibonacci":
            arg1 = str(30)
            arg2 = "Results/" + files
            code = "/fib.py"

        cmdFib = ["python", os.getcwd() + code, arg1, arg2]
        subp = subprocess.Popen(cmdFib)
        pid = subp.pid
        print("Process with pid: " + str(pid))    #log
        process= {"id": request["id"],
                  "type": request["type"],
                  "pid": pid,
                  "started": True,
                  "finished": False}
        g = open("Files/InProgress/process" + str(i), "w+")
        json.dump(process, g)
        g.close()
        f.close()
        os.remove(pathReq + files)

def checkForFinishedProcesses():
    files = os.listdir(pathInProg)

    j = len(os.listdir(pathFinish))
    for i in range(len(files)):
        print(files[i])
        f = open(pathInProg + files[i], "r")
        process = json.load(f)
        #Chech if the process is running
        finished = False
        try:
            os.kill(process["pid"], 0)
        except OSError:
            finished = True
        if finished:
            process["finished"]: True
            g = open(pathFinish + "process"+ str(j), "w+")
            json.dump(process, g)
            g.close()
            f.close()
            os.remove(pathInProg + files[i])
            print("process " + str(process["pid"]) + " has finished")
        else:
            print("process " + str(process["pid"]) + " has not finished")
        j = j+1



if len(os.listdir(pathReq)) == 0 and (os.listdir(pathInProg)) == 0: #len(os.list...)
    FileGenerator.generateNewRequests()
checkForRequests()
checkForFinishedProcesses()
