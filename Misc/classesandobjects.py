### real world things being turned into abstract models in code#
## ex buildings cities, cars, people, etc

# class is a blueprint for creating objects

# class person:
# #### def __init__ is a constructor
# ### constructor is used to initialize the attributes of a class aka person
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age  
#         self.height = height


#     def __str__(self):
#         print()

# person1 = person('Mike', 25, 180)
# print(person1.name)
# print(person1.age)
# print(person1.height)

# person1.name = 'henry'
# print(person1.name)

# del person1


###############

class One_piece:
    def __init__(self, name, bounty, pirate_crew):
        self.name = name
        self.bounty = bounty
        self.pirate_crew = pirate_crew

    def luffy(self):
        strw_luffy = One_piece('Monkey D. Luffy', 1.5, 'Straw Hat Pirates')
        return strw_luffy
    
    def zoro(self):
        strw_zoro = One_piece('Roronoa Zoro', 320, 'Straw Hat Pirates')
        return strw_zoro
    
    def nami(self):
        strw_nami = One_piece('Nami', 66, 'Straw Hat Pirates')
        return strw_nami
    
    def usopp(self):
        strw_usopp = One_piece('Usopp', 30, 'Straw Hat Pirates')
        return strw_usopp
    
    def sanji(self):
        strw_sanji = One_piece('Sanji', 32, 'Straw Hat Pirates')
        return strw_sanji
    
    def chopper(self):
        strw_chopper = One_piece('Ton tony chopper', 'unknown', 'straw hat pirates')
        return strw_chopper
    
    def robin(self):
        strw_robin = One_piece('Nico Robin', 100, 'Straw Hat Pirates')
        return strw_robin
    
    def franky(self):
        strw_franky = One_piece('Franky', 60, 'Straw Hat Pirates')
        return strw_franky
    
    def brook(self):
        strw_brook = One_piece('Brook', 40, 'Straw Hat Pirates')
        
    

    