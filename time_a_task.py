import time
#import MySQLdb

taskName = ""
start = 0
day = 0
hour = 0
minutes = 0
seconds = 0

def beginTask():
    start = time.perf_counter()
    print(taskName, "has begun")

def endTask():
    input_var = input("End task?: ")
    print(taskName, "as ended. Here is a summary of your work period:")
    elapsedSeconds = time.perf_counter() - start
    convertSeconds(elapsedSeconds)

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
    print('{:.0f}'.format(day),"d", '{:.0f}'.format(hour),"h", '{:.0f}'.format(minutes),"m", '{:.0f}'.format(seconds),"s")


print("Welcome to time_a_task")
taskName = input("What is the name of the task? ")
beginTask()
endTask()
