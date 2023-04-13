#### syncrhonization how to use multiple threads at once that try to access same resource, how  to not run into errors

##ocking concept
import threading
import time

x = 8192

lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    ## global lets me change the variable in the global scope
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print('reached the max!')
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /=2
        print(x)
        time.sleep(1)
    print('reached the min')
    lock.release()

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()


###showcasing an example of an infinite threading loop you dont want
### caused by one func trying to double other trying to halve^^^

## trivial example just showcasing how locking works

### semaphores limit access to resource to a max value

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_num):
    print(f'{thread_num} is trying to access!')
    semaphore.acquire()
    print(f'{thread_num} was granted access')
    time.sleep(10)
    print(f'{thread_num} is now releasing')
    semaphore.release()

for thread_num in range(1, 11):
    t = threading.Thread(target=access, args=(thread_num,))
    ### ^^^ sets the target to the access function and passes thread_num as an argument 
    t.start()
    time.sleep(1)


