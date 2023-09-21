import os
import threading

class ThreadedSearch:
    def __init__(self, dir, file_name):
        self.dir = dir
        self.file_name = file_name
        self.file_list = []

    def search_save(self):
        for root, files in os.walk(self.dir):
            for file in files:
                if file == self.file_name:
                    self.file_list.append(os.path.join(root, file))
        return self.file_list
    
``
    