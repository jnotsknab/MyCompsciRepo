#Author: Jonathan Bankston
#KUID: 3097029
#Date: 3/5/23
#Lab: lab05
#Last modified: 3/5/23
#Purpose: This program stores and navigates through search history with various commands.
history = []
index = -1

def program_state():
    return True


while program_state():
    inp = input("Command: ")
    command = inp.split(" ")
    if(command[0] == "NAVIGATE"):
        index += 1
        history = history[0:index]
        history.append(command[1])
    elif(command[0] == "BACK"):
        if(index > 0):
            index -= 1
    elif(command[0] == "FORWARD"):
        if (index < len(history) - 1):
            index += 1
    elif(command[0] == "HISTORY"):
        print("OLDEST")
        print("============")
        for idx, val in enumerate(history):
            if(idx == index):
                print(val + " <==")
            else:
                print(val)
        print("============")
        print("NEWEST")
    elif(command[0] == "EXIT"):
        break