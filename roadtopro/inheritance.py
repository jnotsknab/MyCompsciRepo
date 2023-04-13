##one general class with others that inherit from this class
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def __str__(self):
        return f'Name: {self.name} Age: {self.age} Height: {self.height} '
    
    def get_older(self, years):
        self.age += years
    
    ##can define subclass which inherits for something such as worker which is a person

# class Worker:
#     def __init__(self, name, age, height, salary)
        
        #^^^ not reasonable should inherit instead

class Worker(Person):
    def __init__(self, age, name, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary
    def __str__(self):
        text = super(Worker, self).__str__()
        text += f'Salary: {self.salary}'
        return text
    
    def yearly_pay(self):
        return self.salary * 12
    
worker1 = Worker(40, 'henry', 164, 164000)
print(worker1)
print(worker1.yearly_pay())


### ^^^ can inherit again and again
### class worker inherits from class person
####operator overloading ()
##Operator overloading in Python refers to the ability to redefine the behavior of built-in operators (like +, -, *, /, etc.) for custom classes. By implementing specific methods in your class, you can change how the operators work when applied to instances of that class. 

###useful in certain situations like when you want to add vectors

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


### when overloading you have the object itself which is self(vecotr in this case) then you have something else which you are adding to(other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'X {self.x} Y: {self.y}'
    
v1 = Vector(2, 5)
v2 = Vector(6, 3)

print(v1)
print(v2)
v3 = v1 - v2
print(v3)


### how operator overloading works^^^^
## __add__ and __sub__ etc


