'''Using Python Selenium Automation and the URL https://www.instagram.com/guviofficial/.
kindly do the following mentioned tasks:-
1) Use either Relative or Absolute XPATH only for the task.
2) Extract the total number of Followers and Following from the URL mentioned above.'''

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Instagram:

    def __init__(self):
        self.url = 'https://www.instagram.com/guviofficial/'
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def open_url(self):
        self.driver.get(self.url)
        print("Opening url successfull")
        sleep(5)

    def extract_followers_following(self):
        try:
            followers_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span')))
            followers = followers_element.text

            following_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/section/main/div/header/section/ul/li[3]/button/span/span')))
            followings = following_element.text

            print(f"Number of followers: {followers}")
            print(f"Number of followings: {followings}")
        except NoSuchElementException as e:
            print(f"Error extracting followers/followings: {e}")

    def shutdown(self):
        self.driver.quit()
        print("Browser closed")

insta = Instagram()

insta.open_url()

insta.extract_followers_following()

insta.shutdown()
