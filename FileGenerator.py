import json

path = "Files/Requests/"
file = "request"
extension = ".json"

def generateNewRequests():
    print("Generating example files...\n")
    for i in range(0, 10):
        f = open(path+file+str(i)+extension, "w")
        process = {"id": i,
                   "type": "fibonacci",
                   "pid": 0,
                   "started": False,
                   "finished": False}
        json.dump(process, f)
        #f.write(process) #llibreria jason
        f.close()