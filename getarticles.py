from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getarticles:
    def __init__(self, driver):
        self.driver=driver
        self.driver.get('https://www.instagram.com')
        self.hrefs=[]
        try:
            btn=self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
            btn.click()
        except:
            pass
        # body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm
             # 12 pages/loading

    def get_articles(self):
        countLike=0
        
        for i in range(100):
            
            time.sleep(1)
            self.articlediv=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html')))
            
            print("\nScroll: " +str(i+1))
            print("__________")
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight', self.articlediv)
            # time.sleep(2)
            # self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight', self.articlediv)
            
            for p in range(6):
                if p<=3:
                    p+=3
                p+=1
                time.sleep(3)
                try:
                    print('Article: '+str(p))
                    try:
                        like_btn=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'article._8Rm4L:nth-child({}) > div:nth-child(4) > section:nth-child(1) > span:nth-child(1) > button:nth-child(1)'.format(str(p)))))
                    except:
                        print("---Break---")
                        break
                    like_btn.click()
                    countLike+=1
                    print("Current liked article: " + str(countLike))
                except:
                    print("Sorry, Unable to like this article")

    
    # def like_articles(self):
