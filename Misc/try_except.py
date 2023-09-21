#Author: Jonathan Bankston
#KUID: 3097029
#Date: 4/26/23
#Lab: lab11
#Last modified: 4/27/23
#Purpose: This program stores data from a dmv text file and allows the user to interact with the sorted data in various ways.


class DriversLicense:

    '''Initializes the drivers license object'''

    def __init__(self, license_number, first_name, last_name, age, voter_status):
        self._license_number = int(license_number)
        self._first_name = first_name
        self._last_name = last_name
        self._age = int(age)
        self._voter_status = voter_status == "Y"



    def __lt__(self, other):

        '''Returns true if the license number of the first object is less than the license number of the second object'''

        return self._license_number < other._license_number
    

    def __gt__(self, other):

        '''Returns true if the license number of the first object is greater than the license number of the second object'''

        return self._license_number > other._license_number


    def __le__(self, other):

        '''Returns true if the license number of the first object is less than or equal to the license number of the second object'''

        return self._license_number <= other._license_number
    

    def __ge__(self, other):

        '''Returns true if the license number of the first object is greater than or equal to the license number of the second object'''

        return self._license_number >= other._license_number


    def __eq__(self, other):

        '''Returns true if the license number of the first object is equal to the license number of the second object'''

        return self._license_number == other._license_number
    

    def __ne__(self, other):

        '''Returns true if the license number of the first object is not equal to the license number of the second object'''

        return self._license_number != other._license_number
    

    def __str__(self):

        '''Returns a string representation of the object'''

        return f"{self._last_name}, {self._first_name} ({self._age}): {self._license_number} {'registered' if self._voter_status else 'not registered'}"
    

    def __repr__(self):

        '''Shows how to recreate the object'''

        return f"DriversLicense({self._license_number}, {self._first_name}, {self._last_name}, {self._age}, {self._voter_status})"
    

class Dmv:
    def __init__(self, file_name):

        '''Initializes the dmv object'''

        self._licenses = self._read_file(file_name)


    def _read_file(self, file_name):

        '''Reads the dmv file and returns a list of drivers licenses'''

        licenses = []
        with open(file_name, "r") as file:
            for line in file:
                license_number, first_name, last_name, age, voter_status = line.split()
                licenses.append(DriversLicense(license_number, first_name, last_name, age, voter_status))
        return licenses
    

    
    def run_prog(self):

        '''Runs the body of the program'''

        while True:
            choice = self._print_menu()
            if choice == "1":
                self._all_drivers()
            elif choice == "2":
                self._young_unregistered()
            elif choice == "3":
                self._last_initial()
            elif choice == "4":
                self._drivers_age()
            elif choice == "5":
                print("Program ending...")
                exit()
            else:
                print("Invalid choice, please try again.")

    
    def _print_menu(self):

        '''Prints the menu and returns the user's choice'''

        print("\nSelect an option:")
        print("1) Print all Drivers Info, sorted by drivers license numbers")
        print("2) Print all young, unregistered voters")
        print("3) Print drivers by last initial")
        print("4) Print drivers of a specific age")
        print("5) Quit")
        return input("Enter your choice: ")

    
    def _all_drivers(self):

        '''Prints all drivers in the dmv file'''

        for driver in sorted(self._licenses):
            print(driver)

    
    def _young_unregistered(self):

        '''Prints all drivers between the ages of 18 and 24 who are not registered to vote'''

        for driver in self._licenses:
            if 18 <= driver._age <= 24 and not driver._voter_status:
                print(driver)

    
    def _last_initial(self):

        '''Prints all drivers whose last name starts with a specific letter'''

        initial = input("Enter last initial: ").upper()
        found = False
        for driver in self._licenses:
            if driver._last_name[0].upper() == initial:
                print(driver)
                found = True
        if not found:
            print("No records")


    def _drivers_age(self):

        '''Prints all drivers of a specific age'''

        age = int(input("Enter age: "))
        found = False
        for driver in self._licenses:
            if driver._age == age:
                print(driver)
                found = True
        if not found:
            print("No records")



def main():

    '''Calls the Dmv class and hands off control to the Dmv class'''

    file_name = input('Enter a file name: ')
    my_DMV = Dmv(file_name)
    my_DMV.run_prog()


if __name__ == '__main__':
    main()
