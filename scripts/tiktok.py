from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class automtise_tiktok():
    def __init__(self,tiktoklink):
        self.tiktok_link=tiktoklink
        self.driver=webdriver.Chrome(service=Service("D:\\projects\\automation_lucky_boom\\chrome_drivere\\chromedriver.exe"))
        self.actions = ActionChains(self.driver)


    def login_tt(self):
        print(self.driver.window_handles)
        self.driver.get(self.tiktok_link)
        sleep(3)
        self.close_tt=self.driver.find_element(By.XPATH,"""//*[@id="login-modal"]/div[2]""")
        self.close_tt.click()
        sleep(2)
        self.login_button=self.driver.find_element(By.XPATH,"""//*[@id="header-login-button"]""").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"""//*[@id="loginContainer"]/div/div/div/div[4]/div""").click()
        self.windows=self.driver.window_handles
        sleep(3)
        self.driver.switch_to.window(self.windows[-1])
        self.input_email=self.driver.find_element(By.XPATH,"""//*[@id="identifierId"]""")
        self.input_email.send_keys("peshcka.vlad@gmail.com")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.next_button=self.driver.find_element(By.XPATH,"""//*[@id="identifierNext"]/div/button""")
        sleep(3)
        self.next_button.click()
        sleep(3)
        self.driver.switch_to.window(self.windows[-1])
        self.password=self.driver.find_element(By.XPATH,"""//*[@id="password"]/div[1]/div/div[1]/input""")
        self.password.send_keys("12345Qwerty")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        self.driver.find_element(By.XPATH,"""//*[@id="passwordNext"]/div/button""").click()
        sleep(30)