import os,subprocess
import FileGenerator

pathReq = "Files/Requests/"
pathInProg = "Files/InProgress/"
pathFinish = "Files/Finished/"

def checkForRequests():
    files = os.listdir(pathReq)
    for i in range(files.__len__()):
        print(files[i])
        f = open(pathReq + files[i], "r")
        #Reads a string and transforms it to a Dictionary
        request = eval(f.read())
        #Avaluate the type of process requested
        if(request["type"] is "fibonacci"):
            arg1 = str(30)
            arg2 = "Results/"+ files[i]
            code = "/fib.py"

        cmdFib = ["python", os.getcwd() + code, arg1, arg2]
        subp = subprocess.Popen(cmdFib)
        pid = subp.pid
        print("Process with pid: "+str(pid))
        process= {"type":request["type"],
                        "id": request["id"],
                        "pid":pid,
                        "started":1,
                        "finished":0}
        g = open("Files/InProgress/process"+str(i), "w+")
        g.write(process.__str__())
        g.close()
        f.close()
        os.remove(pathReq + files[i])

def checkForFinishedProcesses():
    files = os.listdir(pathInProg)

    j = os.listdir(pathFinish).__len__()
    for i in range(files.__len__()):
        print(files[i])
        f = open(pathInProg + files[i], "r")
        process = eval(f.read())
        #Chech if the process is running
        finished = False
        try:
            os.kill(process["pid"], 0)
        except OSError:
            finished = True
        if finished:
            process["finished"]: 1
            g = open(pathFinish + "process"+ str(j), "w+")
            g.write(process.__str__())
            g.close()
            f.close()
            os.remove(pathInProg + files[i])
            print("process "+ str(process["pid"]) + " has finished")
        else:
            print("process "+ str(process["pid"]) +" has not finished")
        j = j+1



if os.listdir(pathReq).__len__() == 0 and os.listdir(pathInProg).__len__() == 0:
    FileGenerator.generateNewRequests()
checkForRequests()
checkForFinishedProcesses()
