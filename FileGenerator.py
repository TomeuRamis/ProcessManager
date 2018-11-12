import os

path = "Files/Requests/"
file = "request"
extension = ".txt"

def generateNewRequests():
    print("Generating example files...\n")
    for i in range(0,10):
        f = open(path+file+str(i)+extension, "w")
        process = {"id": i,
                   "type":"fibonacci",
                   "started":0,
                   "finished":0}
        f.write(process.__str__())
        f.close()