import os
import subprocess
import FileGenerator
import json

pathReq = "Files/Requests/"
pathInProg = "Files/InProgress/"
pathFinish = "Files/Finished/"


def checkForRequests():  # try
    for i, file in enumerate(os.listdir(pathReq)):
        print(file)  # log
        f = open(pathReq + file, "r")
        # Reads a string and transforms it to a Dictionary
        request = json.load(f)
        print(str(request))
        # Avaluate the type of process requested
        if request["type"] == "fibonacci":
            arg1 = str(30)
            arg2 = "Results/" + file
            code = "/fib.py"

        cmdFib = ["python", os.getcwd() + code, arg1, arg2]
        subp = subprocess.Popen(cmdFib)
        pid = subp.pid
        print("Process with pid: " + str(pid))  # log
        process = {"id": request["id"],
                   "type": request["type"],
                   "pid": pid,
                   "started": True,
                   "finished": False}
        g = open("Files/InProgress/process" + str(i), "w+")
        json.dump(process, g)
        g.close()
        f.close()
        os.remove(pathReq + file)


def checkForFinishedProcesses():
    j = len(os.listdir(pathFinish))
    for i, file in enumerate(os.listdir(pathInProg)):
        print(file)
        f = open(pathInProg + file, "r")
        process = json.load(f)
        # Chech if the process is running
        finished = False
        try:
            os.kill(process["pid"], 0)
        except OSError:
            finished = True
        if finished:
            process["finished"]: True
            g = open(pathFinish + "process" + str(j) + ".json", "w+")
            json.dump(process, g)
            g.close()
            f.close()
            os.remove(pathInProg + file)
            print("process " + str(process["pid"]) + " has finished")
        else:
            print("process " + str(process["pid"]) + " has not finished")
        j = j + 1


if len(os.listdir(pathReq)) == 0 and (os.listdir(pathInProg)) == 0:  # len(os.list...)
    FileGenerator.generateNewRequests()
checkForRequests()
checkForFinishedProcesses()
