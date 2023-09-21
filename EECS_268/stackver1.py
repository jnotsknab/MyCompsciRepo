from node import Node
class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, entry):
        new_node = Node(entry)
        new_node.next = self._top
        self._top = new_node

    def pop(self):
        if self._top is None:
            raise RuntimeError("Cannot pop an empty stack")
        else:
            return self._top.entry
    
    def is_empty(self):
        return self._top is None