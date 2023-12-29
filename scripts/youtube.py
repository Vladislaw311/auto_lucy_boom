from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class automation():
    def __init__(self,link_youtube):
        self.driver =webdriver.Chrome(service=Service("D:\\projects\\automation_lucky_boom\\chrome_drivere\\chromedriver.exe"))
        self.link_youtube=link_youtube
        self.action=ActionChains(self.driver)
        self.options=Options()
    def login_in_site(self):
        with open("accounts", "r") as f:
            self.options.add_argument("--window-size=1366,768")
            for i in f:
                index_sapce = i.find(" ")
                self.log = i[:index_sapce:]
                self.password = i[index_sapce + 1::]
                self.driver.get(self.link_youtube)
                sleep(3)
                self.loggin_button=self.driver.find_element(By.XPATH,"""//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]""")
                self.loggin_button.click()
                sleep(3)
                self.input1=self.driver.find_element(By.XPATH,"""//*[@id="identifierId"]""")
                self.input1.send_keys(self.log)
                self.next_button=self.driver.find_element(By.XPATH,"""//*[@id="identifierNext"]/div/button""")
                sleep(3)
                self.next_button.send_keys(Keys.ENTER)
                sleep(3)
                self.passw=self.driver.find_element(By.XPATH,"""//*[@id="password"]/div[1]/div/div[1]/input""")
                self.passw.send_keys(self.password)
                self.input2=self.driver.find_element(By.XPATH,"""//*[@id="passwordNext"]/div/button""")
                self.input2.click()
                sleep(3)


    def add_video(self):
        self.add_video_button=self.driver.find_element(By.XPATH,"""//*[@id="button"]/a""")
        self.add_video_button.click()
        sleep(3)
        self.add_video_button1=self.driver.find_element(By.XPATH,"//yt-formatted-string[contains(@id, 'label')]")
        print(self.add_video_button1.is_displayed())
        self.add_video_button1.click()
        sleep(10)
        print(self.driver.window_handles)
        self.close1=self.driver.find_element(By.ID,"close-button")
        print(self.close1.is_displayed())
        self.close1.click()
        # self.action.move_to_element(self.close1).click().perform()
        sleep(5)
        # self.shorts=self.driver.find_element(By.XPATH,"""//*[@id="content"]/input""")
        # self.input=self.driver.find_element(By.XPATH,"""//*[@id="content"]/input""")
        # self.input.send_keys("D:\\projects\\automation_lucky_boom\\vidio\\video_2023-12-15_13-42-39.mp4")
        # sleep(3)
        # self.not_children=self.driver.find_element(By.XPATH,"""//*[@id="offRadio"]""")
        # print(self.not_children.is_displayed())
        # self.not_children.click()
        sleep(400)