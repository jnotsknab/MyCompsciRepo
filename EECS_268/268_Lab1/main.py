#Jonathan Bankston
#EECS 268
#Lab 1
#9/1/23 - 9/4/23
#University of Kansas


from Executive import parse_board_games, print_all_games, print_games_from_year, print_ranking_range, print_by_playtime, print_rating_diff

def main():
    ### main function which prints menu and pulls data from given file from user in order to execute the program.
    filename = input("Enter the board game filename: ")
    games = parse_board_games(filename)
    
    while True:
        print("\nUser's Menu")
        print("1. Print all games ")
        print("2. Print all games from a specific year")
        print("3. Print a rank range")
        print("4. Students VS Dr. Gibbons")
        print("5. Print based on time to play")
        print("6. Exit program")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print_all_games(games)
        elif choice == "2":
            year = int(input("Enter the year: "))
            print_games_from_year(games, year)
        elif choice == "3":
            start, end = map(float, input("Enter the rank range (start-end): ").split("-"))
            print_ranking_range(games, start, end)
        elif choice == "4":
            diff = float(input("Enter the rating difference threshold: "))
            print_rating_diff(games, diff)
        elif choice == "5":
            max_playtime = int(input("Enter the max play time: "))
            print_by_playtime(games, max_playtime)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()