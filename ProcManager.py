import os
import subprocess
import json
import logging

absPath = os.getcwd()
pathReq = absPath+"/Files/Requests/"
pathInProg = absPath+"/Files/InProgress/"
pathFinish = absPath+"/Files/Finished/"

logging.basicConfig(filename='example.log',
                    level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def checkForRequests():
    try:
        for i, file in enumerate(os.listdir(pathReq)):
            logging.info("Processing request: " + file)
            f = open(pathReq + file, "r")
            # Reads a string and transforms it to a Dictionary
            request = json.load(f)
            # Evaluate the type of process requested
            if request["type"] == "fibonacci":
                arg1 = str(30)
                arg2 = "Results/" + file
                code = "/fib.py"
                cmdFib = ["python", os.getcwd() + code, arg1, arg2]

            if request["type"] == "wait":
                arg1 = str(20)
                code = "/wait.py"
                cmdFib = ["python", os.getcwd() + code, arg1]

            subp = subprocess.Popen(cmdFib)
            pid = subp.pid
            logging.info("Created new process with pid: " + str(pid) + "\n")
            request["pid"] = pid
            request["started"] = True
            g = open(pathInProg + "process" + str(i) + ".json", "w+")
            json.dump(request, g)
            g.close()
            f.close()
            os.remove(pathReq + file)
    except IOError:
        logging.error("IO Error has occurred: Directory/File not found")


def checkForFinishedProcesses():
    try:
        j = len(os.listdir(pathFinish))
        for i, file in enumerate(os.listdir(pathInProg)):
            logging.info("Checking process: " + file)
            f = open(pathInProg + file, "r")
            process = json.load(f)

            # Check if the process is running
            finished = False
            try:
                os.kill(process["pid"], 0)
            except OSError:
                finished = True

            if finished:
                process["finished"] = True
                g = open(pathFinish + "process" + str(j) + ".json", "w+")
                json.dump(process, g)
                g.close()
                f.close()
                os.remove(pathInProg + file)
                logging.info("process " + str(process["pid"]) + " has finished\n")
            else:
                logging.info("process " + str(process["pid"]) + " has not finished\n")

            j = j + 1
    except IOError:
        logging.error("IO Error has occurred: Directory/File not found")