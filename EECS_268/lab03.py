from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def insert(self, index, entry):
        # sourcery skip: extract-method, for-index-underscore
        if index < 0 or index > self.length:
            raise IndexError("Entry is out of bounds")
        elif index == 0:
            new_node = Node(entry)
            new_node.next = self.head
            self.head = new_node

            self.length +=1

        elif index == self.length:
            new_node = Node(entry)
            new_node.next = None
            temp_last = self.head

            while temp_last.next is not None:
                temp_last = temp_last.next

            temp_last.next = new_node

        else:
            new_node = Node(entry) 
            jumper_node = self.head

            for i in range(index - 1):
                jumper_node = jumper_node.next

            target = jumper_node.next

            jumper_node.next = new_node
            new_node.next = target
            self.length += 1








