from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getarticles

username='Put Your Username'
password='Put Your Password'
driver = 0

def main():
    global driver
    print('running script..')
    driver = webdriver.Chrome('D://a1/software_installer/chromedriver_win32/chromedriver.exe')
    l=login.Login(driver, username, password)
    l.signin()
    print("login succeed...!")
    time.sleep(10)
    ga=getarticles.Getarticles(driver)
    ga.get_articles()

if __name__ =='__main__':
    main()