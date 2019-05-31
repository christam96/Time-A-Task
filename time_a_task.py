import time
import os

# Imports for replace()
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

dbFile = "db.txt"

taskName = ""
start = 0
day = 0
hour = 0
minutes = 0
seconds = 0
elapsedSeconds = 0

prevTime = 0
newTime = 0
formatTime = 0

def beginTask():
    global start
    start = time.perf_counter()
    print("Enjoy your work session!")

def endTask():
    global taskName
    input_var = input("End task?: ")
    print("Summary of your last work period:")
    elapsedSeconds = time.perf_counter() - start
    convertSeconds(elapsedSeconds)
    updateDB(taskName, elapsedSeconds)
    print("The total time spent on this task is: ")
    convertSeconds(getTime(taskName))

def convertSeconds(elapsedSeconds):
    day = elapsedSeconds/(24*3600)
    if day < 1:
        day = 0
    elapsedSeconds = elapsedSeconds % (3600)
    hour = elapsedSeconds/3600
    if hour < 1:
        hour = 0
    elapsedSeconds %= 3600
    minutes = elapsedSeconds/60
    if minutes < 1:
        minutes = 0
    elapsedSeconds %= 60
    seconds = elapsedSeconds
    print('{:.0f}'.format(hour),"h", '{:.0f}'.format(minutes),"m", '{:.0f}'.format(seconds),"s")

def checkDB(taskName):
    global prevTime
    dbString = open(dbFile, 'r')
    dbString.read()
    if taskName in open(dbFile).read():
        # Task already exists
        lines = [line.rstrip('\n') for line in open(dbFile)]
        for task in lines:
            split = task.split(":")
            name = split[0]
            time = split[1]
            if name == taskName:
                prevTime = int(time)
    else:
        # Task does not yet exist
        if os.stat(dbFile).st_size > 0:
            with open(dbFile, 'a') as db:
                print(taskName + " was added to the database")
                db.write('\n' + taskName  + ":0")
        else:
            with open(dbFile, 'a') as db:
                print(taskName + " was added to the database")
                db.write(taskName  + ":0")

def updateDB(taskName, elapsedSeconds): 
    global prevTime
    global newTime
    global formatTime, dbFile
    lines = [line.rstrip('\n') for line in open(dbFile)]
    for task in lines:
        split = task.split(":")
        name = split[0]
        prevTime = split[1]
        if name == taskName:
            newTime = int(prevTime) + elapsedSeconds
            formatTime = '{:.0f}'.format(newTime)
            newTask = taskName + ":" + str(formatTime)
            with open(dbFile, 'a'):
                replace(task, newTask)

def replace(pattern, subst):
    global dbFile
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(dbFile) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Move new file
    move(abs_path, dbFile)

def getTime(taskName):
    lines = [line.rstrip('\n') for line in open('db.txt')]
    for task in lines:
        split = task.split(":")
        name = split[0]
        time = split[1]
        if name == taskName:
            return int(time)
    
print("----------------------------\n         WORK LOGGER \n----------------------------")
taskName = input("What is the name of the task? ")
taskName = taskName.lower()
checkDB(taskName)
beginTask()
endTask()