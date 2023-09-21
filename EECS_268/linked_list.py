from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, index, entry):
        if index  < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        elif index == 0:
            new_node = Node(entry)
            new_node.next = self.head
            self.head = new_node

            self.length += 1
        else:
            new_node = Node(entry)
            jumper = self.head

            for i in range(index - 1):
                jumper = jumper.next

            target = jumper.next

            jumper.next = new_node
            new_node.next = target
            self.length += 1





    def get_entry(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        else:
            jumper = self.head

            for i in range(index):
                jumper = jumper.next

            return jumper.entry
            
                
