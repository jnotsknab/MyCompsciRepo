##EECS 268 Lab2
##Jonathan Bankston 3097029
##university of kansas
##9/17/23
##node class
class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

#stack class that push, pops, peeks, and checks if the stack is empty
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, entry):
        if self.top is None:
            self.top = Node(entry)
        else:
            node = Node(entry)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        else:
            delete = self.top
            data = self.top.entry
            self.top = self.top.next
            del delete
            return data
    
    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.entry
    
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

#Queue class to add and remove items to queue, able to also peek at top of queue and check if empty
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, entry):
        if self.head is None:
            self.head = Node(entry)
            self.tail = self.head
        else:
            self.tail.next = Node(entry)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            delete = self.head
            data = self.head.entry
            self.head = self.head.next
            del delete
            return data

    def peek_front(self):
        if self.head is None:
            return None
        else:
            return self.head.entry

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

# main function
def main():
    file_name = input("what is the name of the file? ")
    file = open(file_name, 'r')
    statements = file.readlines()

    stack = Stack()
    queue = Queue()

    stack.push("main")
    for stmt in statements:
        cmd = stmt.split()
        if cmd[0] == "START":
            queue.enqueue(cmd[1])
            print(cmd[1], "added to queue")
        elif cmd[0] == "CALL":
            process = queue.dequeue()
            stack.push(cmd[1])
            print(process, "calls", stack.pop())
        elif cmd[0] == "RETURN":
            if stack.peek() == "main":
                print(queue.peek_front(), "returned back from main")
            else:
                while not stack.is_empty():
                    queue.enqueue(stack.pop())
            break
    while not queue.is_empty():
        print(queue.dequeue(), "process has ended")

    


#calls main function
if __name__ == "__main__":
    main()