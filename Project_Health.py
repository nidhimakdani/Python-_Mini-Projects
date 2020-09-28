
import datetime
def gettime():
    return datetime.datetime.now()

print("HEALTH MANAGEMENT SYSTEM")

print("Enter Your Name ")
name = input()

def choice(val):
    if val==1:
        data=int(input("Press 1 for Enter Excersise Data and 2 for Enter Diet Data "))
        if(data==1):
            value=input("Write Here\n")
            with open(name+"ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Data is Stored")
        elif(data==2):
            value = input("Write Here\n")
            with open(name+"diet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Data is Stored")

    elif val==2:
        data=int(input("Enter 1 for Retrive Excersise Data and 2 for Retrive Diet Data "))
        if(data==1):
            with open(name+"ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(data==2):
            with open(name+"diet.txt") as op:
                for i in op:
                    print(i, end="")

dt = int(input("Press 1 for Submit Data and 2 for Retrive Data "))
choice(dt)
