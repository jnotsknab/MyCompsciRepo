# Create a list to store the history
history = []
# Create a pointer to where we are in the history
# Initially it is -1 indicating that there is nothing
index = -1
while(True):
    inp = input("Command: ")
    command = inp.split(" ")
    if(command[0] == "NAVIGATE"):
        # We now have one URL. Increase the index
        index += 1
        # If we are in the middle if history, delete everything after index
        history = history[0:index]
        # Add this new URL
        history.append(command[1])
    elif(command[0] == "BACK"):
        # If there is more than one URL in history, go back
        if(index > 0):
            index -= 1
    elif(command[0] == "FORWARD"):
        # If there is URL ahead, move ahead
        if (index < len(history) - 1):
            index += 1
    elif(command[0] == "HISTORY"):
        print("Oldest")
        print("============")
        # Print history
        for idx, val in enumerate(history):
            # If current index points to current history, print the arrow
            if(idx == index):
                print(val + " <==")
            else:
                print(val)
        print("============")
        print("Newest")
    elif(command[0] == "EXIT"):
        # Quit
        break