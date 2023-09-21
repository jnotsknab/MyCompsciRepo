####################################
#file IO review
# different modes do different things a+ is open for reading/appending
# r = open for read which is default
# w = open for writing
# r+ = open for reading and writing
# w+ = open for read/write, truncate
# a+ = open for read/append

# f = open('test.txt', 'r')
# print(f.name)

# f.close()

# #########################
# #opening files to work within a block
# with open('test.txt', 'r') as f:
#    f_content = f.read(5)
#    print(f_content, end='')
   
#     # for line in f:
#     #     print(line, end='')



#     # f_content = f.read()
#     # print(f_content)

#################################
#more review

# with open('test.txt', 'r') as f:
#     size_read = 5
#     f_contents = f.read(size_read)

#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.rea


##############################
#number guessing game

import random
import sys


def random_number():
    random_number = random.randint(1, 1000)
    return random_number


def guess_number():
    return int(input('Enter a guess between 1 and 1000'))

def accuracy(guess, random_num):
    if guess == random_num:
        return 'You guessed correctly!'
    elif guess > random_num:
        return 'Your guess is too high'
    else:
        return 'Your guess is too low'


def main():
    choice = 0
    while True:
        print('1. Play the game')
        print('2. Quit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            random_num = random_number()
            while True:
                guess = guess_number()
                print(accuracy(guess, random_num))
                if guess == random_num:
                    break
            print(accuracy(guess, random_num))

        elif choice == 2:
            print('game ending...')
            sys.exit()
        else:
            print('invalid choice')


    
if __name__ == '__main__':
    main()


######################
