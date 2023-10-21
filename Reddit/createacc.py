import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import itertools
import selenium.common.exceptions as sel_exceptions
import random
import array

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = selenium.webdriver.Chrome(options = options)

used_emails = []
used_usernames = []
emails = []
usernames = []
passwords = []
email_names = ['alpha',
                'omega',
                'ruby',
                'sapphire',
                'omegraruby',
                'alphasaphhire',
                'artreus',
                'kratos',
                'leai']


def create_acc():

    url = 'https://www.reddit.com/account/register/'
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'regEmail')))
    wait.until(EC.element_to_be_clickable((By.ID, 'regEmail')))
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
    submit_btn = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))

    while True:
        
        for i in range(2):
            username = generate_username(name_of_user = random.choice(email_names))
            
        if username not in used_usernames:
            used_usernames.append(username)
            break

    email_field = driver.find_element(By.NAME, 'email')
    time.sleep(1)
    email_field.send_keys(rand_email())
    time.sleep(5)
    submit_btn.click()

def pw_gen():

    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 12

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
            '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but 
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined 
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to 
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x

    passwords.append(password)
    print(password)
    return password

def rand_email():
    email = f'{generate_username(name_of_user = random.choice(email_names))}@gmail.com'
    emails.append(email)
    print(email)
    return email

def generate_username(name_of_user):
    
    # Constraints 
    minimum_capital_letter = 2
    minimum_specia_char = 2
    minimum_digits = 2
    min_len_of_username = 8
    special_chars = ['#','$','&']

    # variable to store generated username
    username = ""

    # remove space from name of user
    name_of_user = "".join(name_of_user.split())

    # convert whole name in lowercase 
    name_of_user = name_of_user.lower()

    # calculate minimum characters that we need to take from name of user 
    minimum_char_from_name = min_len_of_username-minimum_digits-minimum_specia_char

    # take required part from name 
    temp = 0
    for i in range(random.randint(minimum_char_from_name,len(name_of_user))):
        if temp < minimum_capital_letter:
            username += name_of_user[i].upper()
            temp += 1
        else:
            username += name_of_user[i]

    # temp_list to store digits and special_chars so that they can be shuffled before adding to username 
    temp_list = []
    # add required digits 
    for i in range(minimum_digits):
        temp_list.append(str(random.randint(0,9)))

    # append special characters 
    for i in range(minimum_specia_char):
        temp_list.append(special_chars[random.randint(0,len(special_chars)-1)])

    # shuffle list 
    random.shuffle(temp_list)

    username += "".join(temp_list)

    usernames.append(username)

    return username


create_acc()