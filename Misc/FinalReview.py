### Review for programming 1 final exam

### Boardworks

##One##
# def func1():
#     return 'Jonathan Bankston: games, programming, gf, weed'

# print(func1())


##two##
# def func2():
#     user_input = input('What is your favorite food?')
#     return print(f'{user_input} is so yummy!')

# func2()


##three##

# def area():
#     user_input1 = int(input('What is the width of the rectangle'))
#     user_input2 = int(input('What is the height of the rectangle'))
#     return print(user_input1 * user_input2)

# area()



##four##
# def popup():
#     print('Nicos Pop Shop!!!')
#     price = 25.99
#     dish = 'Burrito'
#     user_input = int(input(f'How many {dish}(s) do you want?'))
#     total = price * user_input
#     return print(f'Your final total will be ${total}. ')

# popup()



##five##
# def bouncer():
#     user_age = int(input('What is your age?'))
#     if user_age <21:
#         return print('Scram Junior')
#     else:
#         return print('Welcome to the pub!')
    
# bouncer()



##six##

# def grades():
#     user_grade = float(input('What is your score?'))
#     if user_grade >= 90:
#         return print('A')
#     elif user_grade >= 80:
#         return print('B')
#     elif user_grade >= 70:
#         return print('C')
#     elif user_grade >= 60:
#         return print('D')
#     else:
#         return print('F') 

# grades()



##seven##
# def grade2():
#     user_grade = float(input('What was your score?'))
#     if user_grade >= 90:
#         return print('A')
#     if user_grade >= 80 and user_grade <= 90:
#         return print('B')
#     if user_grade >= 70 and user_grade <= 80:
#         return print('C')
#     if user_grade >= 60 and user_grade <= 70:
#         return print('D')
#     else:
#         return print('F')
    
# grade2()



##eight##

# def loop():
#     num = 2
#     while num < 25:
#         print(num)
#         num += 2



##nine##

# def loop2():
#     num = -100
#     while num < 101:
#         print(num)
#         num += 1


# loop2()


##ten##

# def loop3():
#     num = 14
#     while num < 50:
#         print(num)
#         num += 7


# loop3()



# def loop4():
#     user_input = input("Enter either q or Q")
#     while user_input.lower() != 'q':
#         user_input = input("Enter either q or Q")


# loop4()
# def a_counter():
#     count = 0
#     user_input = input('Enter a word: ')
#     for index in user_input:
#         if index.lower() == 'a':
#             count += 1
#     return print(count)


# a_counter()



# def board_worklist():
#     float_list = []
#     for index in range(0, 42):
#         user_input = float(input('Enter a floating point number: '))
#         float_list.append(user_input)
    
#     user_thresh = float(input('Enter a floating point number to act as a threshold value: '))
#     for num in float_list:
#         if num >= user_thresh:
#             print(num)

# board_worklist()



# def board_worklist2():
#     float_list = []
#     for index in range(0, 38):
#         user_float = float(input('Enter a floating point number: '))
#         float_list.append(user_float)
#     return print(max(float_list))

# board_worklist2()

# def find_list():
#     int_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]
#     if 5 in int_list:
#         print('Yes')
#     else:
#         print('NO')

# find_list()



# def toy_store():
#     manager_inventory = input('Enter the inventory items seperated by two dashes (--): ')
#     manager_inventory.split('--')
    
#     kid_input = input('Enter the name of the toy you want!:  ')
#     if kid_input in manager_inventory:
#         return print('We have that toy!!!')
#     else:
#         return print('Sorry, that toy isnt avaliable or in stock.')
    
# toy_store()



# def game_search():
#     game_list = []
#     user_input = input('Enter the name of a file youd like to open.')

#     with open(user_input, 'r') as file:
#         for line in file:
#             line = line.strip()
#             game_list.append(line)
    
#     print(game_list)

#     user_game = input('Enter the name of a game youd like to buy: ')
#     if user_game in game_list:
#         return print(f'{user_game} is in stock')
#     else:
#         return print(f'Sorry, {user_game} was not in stock...')
    
# game_search()



# def write():
#     score_list = []
#     for index in range (0, 50):
#         user_float = float(input('Enter a floating point number to act as a score: '))
#         score_list.append(user_float)

#     avg = sum(score_list) / len(score_list)

#     with open('grades.txt', 'w') as file:
#         for float_num in score_list:
#             file.write(str(float_num) + '\n')
#         file.write(f'Average Score = {str(avg)}')


# write()



# def single_line_scores():
#     with open('single_scores.txt', 'r') as file:
#         score_data = file.read()

#     scores = score_data.split()
#     float_scores = []

#     for score in scores:
#         float_scores.append(float(score))


#     score_avg = sum(float_scores) / len(float_scores)
#     print(score_avg)
            

# single_line_scores()



# def grid():
#     grid = []
#     list1 = [2, 4, 6, 8] 
#     list2 = [3, 6, 9, 12]
#     list3 = [4, 8, 12, 16]
#     grid.append(list1)
#     grid.append(list2)
#     grid.append(list3)

#     column1_sum = list1[0] + list2[0] + list3[0]
#     column2_sum = list1[1] + list2[1] + list3[1]
#     column3_sum = list1[2] + list2[2] + list3[2]
#     column4_sum = list1[3] + list2[3] + list3[3]

#     return print(f'C1: {column1_sum}, C2: {column2_sum}, C3: {column3_sum} C4: {column4_sum}')



# grid()


####-----First time functions are actually used in class ^ all other functions i just set up this way for conviencence



# def smaller_num():
#     user_num1 = int(input('Enter any integer: '))
#     user_num2 = int(input('Enter another integer: '))
#     if user_num1 < user_num2:
#         return print(user_num1)
#     elif user_num2 < user_num1:
#         return print(user_num2)
#     elif user_num1 == user_num2:
#         return print(user_num1)
#     else:
#         print('Integers do not meet any criteria..')


# smaller_num()



# def even_odd():
#     user_num = int(input('Enter any integer: '))
#     if user_num % 2 == 0:
#         return True
#     else:
#         return False
    

# print(even_odd())



# def shorter_string(user_string1, user_string2):
#     if len(user_string1) < len(user_string2):
#         return user_string1
#     elif len(user_string2) < len(user_string1):
#         return user_string2
#     else:
#         return user_string1

# ##have to import random in order to randomly select between string1 or 2.
     

# print(shorter_string('jonathan', 'may'))



# def print_repeat(string, num_repeat):
#     for index in range(0, num_repeat):
#         print(string)

# print_repeat('luffy', 500)



# def dict_grades(grades_dict):
#     for value in grades_dict.keys():
#         grades_dict[value] += 20
#     return grades_dict

# grades_dict = {
#     'Alice': 80,
#     'Bob' : 80,
#     'Jon': 99,
#     'May': 99

# }



# print(dict_grades(grades_dict))



# def letter_count(string):
#     letter_countdict = {}
#     for character in string.lower():
#         if character in letter_countdict:
#             letter_countdict[character] += 1
#         else:
#             letter_countdict[character] = 1
#     return letter_countdict


# print(letter_count('myNamEISjONAthanBANKSTon'))




# def rev_sets():
#     user1_likes = input('Enter the things you like (comma seperated): ')
#     user2_likes = input('Enter the things you like (comma seperated): ')

#     user1_list = user1_likes.split(',')
#     user2_list = user2_likes.split(',')

#     user1_set = set(user1_list)
#     user2_set = set(user2_list)


#     for value in user1_set:
#         if value in user2_set:
#             return 'GET MARRIED!!!'
    
#     return 'Sorry you guys have nothing in common.'


# print(rev_sets())



# def rev_sets2():
#     user1_likes = input('Enter some things you like comma seperated')
#     user2_likes = input('Enter some things you like comma seperated')

#     user1_list = user1_likes.split(',')
#     user2_list = user2_likes.split(',')

#     user1_set = set(user1_list)
#     user2_set = set(user2_list)

#     in_common = user1_set.intersection(user2_set)

#     if in_common:
#         return 'GET married!'
#     else:
#         return 'Sorry you guys have nothing in common'
    

# print(rev_sets2())


# import random

# def random_rev():
#     user_num = int(input('Enter a number between 2 and 12 that is not 7: '))
#     di_one = random.randint(1,6)
#     di_two = random.randint(1,6)
#     di_sum = di_one + di_two

#     while di_sum != user_num and di_sum != 7:
#         di_one = random.randint(1,6)
#         di_two = random.randint(1,6)
#         di_sum = di_one + di_two
#         print(f'{di_sum} is your number which is not 7 or the users number, so try again.')
    
#     if di_sum == user_num:
#         return f'You win!: the user number was {user_num} and your number was {di_sum}'
#     elif di_sum == 7:
#         return 'You Lose!'
    

# print(random_rev())


# class Student:
#     def __init__(self, names, gpa, major):
#         self.names = names
#         self.gpa = gpa
#         self.major = major



# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def __str__(self):
#         return f'The area of the rectangle is {self.area()} and the perimeter is {self.perimeter()}'

    
#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width * 2) + (self.height * 2)
    

# my_rectangle = Rectangle(10, 20)
# print(my_rectangle)



# class Account:
#     def __init__(self):
#         self._balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             #amount is invalid
#             #we'll learn an appropriate
#             #reaction. For now, we'll
#             #do nothing
#             pass

#     def withdraw(self, amount):
#         if amount <= self._balance and amount > 0:
#             self._balance -= amount
#             return print(f'You withdrew ${amount} out of your account... your remaining balance is  ${self._balance}. ')
#         else:
#             return print('Sorry you tried to withdraw more than your balance..')
        
#     def __repr__(self):
#         return f'Account({self._balance})'
    

    
    
# account_test = Account()
# account_test.deposit(500)
# account_test.withdraw(400)
# account_test.withdraw(500)



# def try_age():
#     try:
#         user_age = int(input('Enter your age: '))
#         return f'You will be {user_age + 978} years old in the year 3000'
#     except:
#         return 'Sorry you entered an invlaid age...'
    


# print(try_age())
        


# def main():
#     user_age = 0
#     while user_age <= 0:
#         try:
#             user_age = int(input('Enter your age: '))
#             if user_age >= 0:
#                 break
#         except:
#             print('Sorry.. invalid age')

#     return 'valid age, all tests passed'

# main() 



# def odds():
#     og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     nw_list = [num for num in og_list if num % 2 != 0]
#     return nw_list

# print(odds())



# def list_comp():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     odd_cubes = [num ** 3 for num in nums if num % 2 != 0]
#     return odd_cubes

# print(list_comp())



# def list_comp2():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     cat_lst = ['cat' for num in nums]
#     return cat_lst

# print(list_comp2())



# def list_comp3():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     above_avg = [num for num in nums if sum(nums)/len(nums) < num]
#     return above_avg

# print(list_comp3())



# age = 12
# adult = True if age >= 18 else False



# print('You are an adult' if adult else 'You are not an adult')



# num = 2000

# print('num is very large' if num > 1000 else 'num is pretty big' if num > 100 else 'num is positive still' if num > 0 else 'this num is negative')

# import random

# list1 = ['dog', 'cat', 'car', 'job']

# choice1 = random.choice(list1)
# choices1 = random.choices(list1, k = 2)
# print(choice1, choices1)



##sets rev


# utensils = {'fork', 'spoon', 'knife'}
# dishes = {'bowl', 'plate', 'cup', 'knife'}


# # utensils.add('napkin')
# # utensils.remove('fork')
# # utensils.clear()
# # utensils.update(dishes)
# # dishes.update(utensils)
# # dinner_table = utensils.union(dishes)

# # for x in dinner_table:
# #     print(x)

# # print(utensils.difference(dishes))
# print(utensils.intersection(dishes))



## dictionary review

# capitals = {'USA': "Washington D.C.", 'india': 'New delhi', 'China': 'bejieng', 'Russia': 'Moscow'}
# print(dir(capitals))
#^^ shows all attributes and methods of dictionaries
# print(capitals.get("USA"))



# if capitals.get('USA'):
#     print('exists')
# else:
#     print('doesnt exist')



# capitals.update({'germany': 'berlin'})
# capitals.update({'USA': 'Detroit'})
# capitals.clear()
# print(capitals)


# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)



# values = capitals.values()
# for value in capitals.values():
#     print(value)



# items = capitals.items()
# for key, value in capitals.items():
#     print(f'{key}: {value}')



























