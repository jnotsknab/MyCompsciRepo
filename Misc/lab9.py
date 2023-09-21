#Author: Jonathan Bankston
#KUID: 3097029
#Date: 3/5/23
#Lab: lab05
#Last modified: 3/5/23
#Purpose: This program stores and navigates through search history with various commands.


import random


class Pokedex:

    '''Initialize the pokedex dictionary'''
    
    def __init__(self):
        self.pokedex = {}
        

    
    def build_pokedex(self, file_name):

        '''Builds the pokedex dictionary and populates it with the pokemon and their jp names'''

        with open(file_name, 'r') as file:
            for line in file:
                poke_list = line.split()
                self.pokedex[poke_list[0]] = poke_list[1]
            return self.pokedex
                


                 

    def build_team(self, pokedex, size = 6, unique = False):

        '''Builds a team of pokemon based on the size and if they are unique or not'''

        team = []
        if unique == True:
            team = random.sample(list(self.pokedex.keys()), k=size)
        else:
            team = random.choices(list(self.pokedex.keys()), k=size)
        return team
                

## crea
    def battle(self, team1, team2):

        '''Battles two teams of pokemon'''

        count = 0
    
        print("+++Team 1+++")
        for item in team1:
            print(item)

        print('')

        print("+++Team 2+++")
        for item in team2:
            print(item)
        
        print('')
        

        for i in range(0, 10):
            count += 1
            rand_winner = random.randint(0, 1)
            print(f'+++Round{count}+++')
            random_pokemon1 = random.choice(team1)
            random_pokemon2 = random.choice(team2)
            print(f'{random_pokemon1} VS {random_pokemon2}')
            print(f'{random_pokemon1} wins!!!') if rand_winner == 0 else print(f'{random_pokemon2} wins!!!')


    def main():

        '''Main function of the program that prints a menu with various options that call the other functions'''

        poke_instance = Pokedex()
        poke_instance.build_pokedex('pokedex.txt')

        print(' 1) Print Pokedex \n 2) Translate \n 3) Build Team \n 4) Battle \n 5) Exit ')
        while True:
            user_input = int(input("Enter an option 1-5 from the menu above..."))
            if user_input == 1:
                for key, value in poke_instance.pokedex.items():
                    print(f'Pokemon US name: {key} Pokemon JP name: {value}')

            if user_input == 2:
                while True: 
                    poke_instance.build_pokedex('pokedex.txt')
                    user_translate = input('Enter a pokemon name to translate: ')
                    if user_translate in poke_instance.pokedex:
                        print(f'{poke_instance.pokedex[user_translate]} is the Japanese name for {user_translate}')
                        break
                    else:
                        print(f'Sorry the name of the pokemon you entered was not found in the Pokedex.')
            
            elif user_input == 3:
                poke_team = poke_instance.build_team(poke_instance.pokedex, size=6, unique=False)
                for item in poke_team:
                    print(item)

            elif user_input == 4:
                team1 = poke_instance.build_team(poke_instance.pokedex, size = 6, unique = False)
                team2 = poke_instance.build_team(poke_instance.pokedex, size = 6, unique = False)
                poke_fight = poke_instance.battle(team1=team1, team2 = team2)
                return poke_fight
            else:
                exit()
    
if __name__ == '__main__':
    Pokedex.main()

            
            
            
            
        

                



        
            

            
        




            




        
        

        
    


