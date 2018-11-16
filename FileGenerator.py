import json
import os

abspath = os.getcwd()
path = abspath+"/Files/Requests/"
file = "request"
extension = ".json"

def generateNewRequests():
    print("Generating example files...\n")
    for i in range(0, 10):
        print("file "+str(i))
        f = open(path+file+str(i)+extension, "w")
        process = {"id": i,
                   "type": "fibonacci",
                   "pid": None,
                   "started": False,
                   "finished": False}
        json.dump(process, f)
        #f.write(process) #llibreria jason
        f.close()
    print("\n")