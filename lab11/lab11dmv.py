import re
class Dmv:

    def __init__(self):
        self.dmv_file = []
        self.license_records = {}

    
    def read_dmv(self):
        with open ('dmv.txt', 'r') as file:
            read_file = file.readlines()
            read_file = [re.sub('\t', ' ', line) for line in read_file]
            read_file = [line.strip() for line in read_file]
            self.license_records.append(read_file)
            
        return self.license_records


    def sort_func(self):
        











                




