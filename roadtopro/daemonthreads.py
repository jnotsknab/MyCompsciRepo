## events and daemon threads

## events are things in python we can trigger

# import threading

# my_event = threading.Event()

# #can trigger or wait for this event

# def my_func():
#     print('waitng for event to trigger')
#     my_event.wait()
#     ## makes the function wait until event is triggered
#     print("Performing actions now...")

# t1 = threading.Thread(target=my_func)
# t1.start()

# x = input('Do you want to trigger the event? y/n)')
# if x == 'y':
#     my_event.set()


## daemon threads run in the background even when the script terminates
## can be used for constant tasks 
import threading
import time

path = 'text.txt'
text = ''

def readfile():
    global path, text
    while True:
        with open('text.txt', 'r') as file:
            text = file.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readfile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()



