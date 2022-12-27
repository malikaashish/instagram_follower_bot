from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

USER_ID = "username"
ACCOUNT_PASSWORD = "password"
ACC = "cristiano"  # account whose followers you want to follow

class InstaFollower:

    def __init__(self):
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        user_field = self.driver.find_element(by="name", value="username")
        user_field.send_keys(USER_ID)
        password_field = self.driver.find_element(by="name", value="password")
        password_field.send_keys(ACCOUNT_PASSWORD)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{ACC}/")
        time.sleep(2)
        followers = self.driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()

        time.sleep(2)

    def follow(self):

        for i in range(2):  # Here adjust no. of followers you want to follow

            button = self.driver.find_element(by="css selector", value="._acas:not(._acao), a._acas:not(._acao), a._acas:not(._acao):visited")
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by="xpath",value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
time.sleep(3)
bot.login()
bot.find_followers()
bot.follow()
