### how to thread: speeds up programs by exectuing multiple tasks at the same time using threads

import threading

# import then define function for threading
def function():
    for x in range(50):
        print('one')

def function2():
    for x in range(50):
        print('two')

# ### not calling function as we arent using it yet were just saying that this is what we want to use it for

# #### starts the threading process on the specified target which is the hello function

# ##can execute two functions at the same time which work in parallel
# ## without threading the funtions are executed top down and the top function finishs all its steps before it moves on
# ### thus with threading we can execute at the same time and bypass this

t1 = threading.Thread(target = function)
t2 = threading.Thread(target = function2)

t1.start()
t2.start()

#must use start function to execute both at the same time

### threading is used a lot in fields such as video games

##waiting for threads

def hello2():
    for x in range(50):
        print('hello')

t1 = threading.Thread(target=hello2)
t1.start()

t1.join()

print('hi bud')

### starts the thread then immediately continues ^^
## if we want to wait for thread to finish we use thread join ^^^

## hi bud is now printed last





