from youtube import automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  time import sleep
from tiktok import automtise_tiktok


# yt = automation(link_youtube="https://www.youtube.com/")
# yt.login_in_site()
# sleep(3)
# try:
#     yt.add_video()
# except Exception as ex:
#     print("нужно ввести номер подождите")


tt = automtise_tiktok(tiktoklink="https://www.tiktok.com/foryou?lang=ru-RU")
tt.login_tt()
