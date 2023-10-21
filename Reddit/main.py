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

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = selenium.webdriver.Chrome(options = options)


def upvote():
    try:

        wait = WebDriverWait(driver, 10)
        upvote_xpath = "//button[@aria-label='upvote']"
        up_button = wait.until(EC.element_to_be_clickable((By.XPATH, upvote_xpath)))
        up_button.click()

    except sel_exceptions.TimeoutException as e:
        print(f'Timeout exception: {e} occured, retrying...')
        script()

    except sel_exceptions.ElementNotInteractableException as e:
        print(f'Unable to interact with element exception: {e}, retyring...')
        script()

    except sel_exceptions.ElementNotVisibleException as e:
        print(f'Element is not visable exception: {e}, retrying...')
        script()

    except KeyboardInterrupt as e:
        print('Script interrupted by user...')
        exit()
        
    except Exception as e:
        print(f'An unknown exception occured: {e}')
        script()


def downvote():
    try:

        wait = WebDriverWait(driver, 10)
        upvote_xpath = "//button[@aria-label='downvote']"
        down_button = wait.until(EC.element_to_be_clickable((By.XPATH, upvote_xpath)))
        down_button.click()

    except sel_exceptions.TimeoutException as e:
        print(f'Timeout exception: {e} occured, retrying...')
        script()

    except sel_exceptions.ElementNotInteractableException as e:
        print(f'Unable to interact with element exception: {e}, retyring...')
        script()

    except sel_exceptions.ElementNotVisibleException as e:
        print(f'Element is not visable exception: {e}, retrying...')
        script()

    except KeyboardInterrupt as e:
        print('Script interrupted by user...')
        exit()
        
    except Exception as e:
        print(f'An unknown exception occured: {e}')
        script()


def logout():
    try:

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='USER_DROPDOWN_ID']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='USER_DROPDOWN_ID']")))
        
        #click on the topright button to open menu
        topright_button = driver.find_element(By.XPATH, "//*[@id='USER_DROPDOWN_ID']")
        topright_button.click()

        #scroll to bottom of menu
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="menu"]')))
        menu = driver.find_element(By.CSS_SELECTOR, '[role="menu"]')
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", menu)
        time.sleep(1)

        #click logout at bottom
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button//*[contains(., 'Log Out')]")))
        logout_button.click()

    except sel_exceptions.TimeoutException as e:
        print(f'Timeout exception: {e} occured, retrying...')
        script()

    except sel_exceptions.ElementNotInteractableException as e:
        print(f'Unable to interact with element exception: {e}, retyring...')
        script()

    except sel_exceptions.ElementNotVisibleException as e:
        print(f'Element is not visable exception: {e}, retrying...')
        script()

    except KeyboardInterrupt as e:
        print('Script interrupted by user...')
        exit()
        
    except Exception as e:
        print(f'An unknown exception occured: {e}')
        script()


def login(user, password):
    try:

        url = 'https://www.reddit.com/login/'

        driver.get(url)
        driver.maximize_window()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']")))
        
        wait.until(EC.presence_of_element_located((By.NAME, "username")))
        wait.until(EC.presence_of_element_located((By.NAME, "password")))

        login_field = driver.find_element(By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']")
        user_field = driver.find_element(By.NAME, "username")
        pass_field = driver.find_element(By.NAME, "password")

        time.sleep(0.5)
        user_field.send_keys(user)
        pass_field.send_keys(password)
        time.sleep(0.5)
        login_field.click()

    except sel_exceptions.TimeoutException as e:
        print(f'Timeout exception: {e} occured, retrying...')
        script()

    except sel_exceptions.ElementNotInteractableException as e:
        print(f'Unable to interact with element exception: {e}, retyring...')
        script()

    except sel_exceptions.ElementNotVisibleException as e:
        print(f'Element is not visable exception: {e}, retrying...')
        script()

    except KeyboardInterrupt as e:
        print('Script interrupted by user...')
        exit()
        
    except Exception as e:
        print(f'An unknown exception occured: {e}')
        script()


def script():
    try:
        
        file_input = input('Enter the name of the txt file that contains info, txt file should be in same path/folder as script: ')
        df = pd.read_csv(file_input)
        user_count = itertools.count(start=0)
        pass_count = itertools.count(start=0)
        url = input('Enter the url of the post you wish to upvote/downvote: ')
        updown_input = int(input('Enter (1) to upvote or (2) to downvote'))

        if updown_input == 1:

            for _ in range(df.shape[0]):
                login(user=df.iloc[next(user_count), 0], password=df.iloc[next(pass_count), 1])
                time.sleep(1)

                driver.get(url)
                time.sleep(0.5)

                upvote()
                time.sleep(0.5)

                logout()
                time.sleep(1.5)

        if updown_input == 2:

            for i in range(df.shape[0]):
                login(user=df.iloc[next(user_count), 0], password=df.iloc[next(pass_count), 1])
                time.sleep(1)

                driver.get(url)
                time.sleep(0.5)

                downvote()
                time.sleep(0.5)

                logout()
                time.sleep(1.5)

    except sel_exceptions.TimeoutException as e:
        print(f'Timeout exception: {e} occured, retrying...')
        script()

    except sel_exceptions.ElementNotInteractableException as e:
        print(f'Unable to interact with element exception: {e}, retyring...')
        script()

    except sel_exceptions.ElementNotVisibleException as e:
        print(f'Element is not visable exception: {e}, retrying...')
        script()

    except KeyboardInterrupt as e:
        print('Script interrupted by user...')
        exit()

    except Exception as e:
        print(f'An unknown exception occured: {e}')
        script()



def main():

    try:
        script()
    except Exception as e:
        print('An exception has occured within main function...')
    finally:
        driver.close()



if __name__ == '__main__':
    main()