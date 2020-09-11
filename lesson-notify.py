#!/usr/bin/python3
#Usage: python3 lesson-notify.py  [Utor Password] [UtorID] [x-path_to_pencil] [x-path_to_lesson]
#You will be notified when b63 tutorial is opened
#Goal: Attempting to get into Thursday's 3:00pm - 5:00pm tutorial, automatically check when a time is available, notifies me -> manually enroll -> Goal complete.

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from sys import argv
import os
import time
  
#These are just examples. Description where to find x-paths are in the github README. 
#path_to_pencil='/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[4]/div/div[3]/div/table/tbody[2]/tr/td[6]/button'
#path_to_lesson='/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/form/table[2]/tbody[3]/tr/td[5]/div/div/div/div[1]/span'

def scrollTo(driver, element):
    '''
    Prerequisite: The element MUST exist on webpage driver
    '''
    while True:
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        try:
            return element
        except:
            continue

if __name__ == "__main__":
    if len(argv)!=5:
        print("Usage: python3 lesson-notify.py  [Utor Password] [UtorID] [x-path_to_pencil] [x-path_to_lesson]")
        os.kill()
        
    try:
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
        driver.get("https://acorn.utoronto.ca/sws/")

        username = driver.find_element_by_id('username')
        username.send_keys(argv[2])

        password = driver.find_element_by_id('password')
        password.send_keys(argv[1])

        loginbutton = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/form/button')
        loginbutton.click()

        driver.get("https://acorn.utoronto.ca/sws/#/courses/0")
        time.sleep(5)

        path_to_pencil = argv[3]
        path_to_lesson = argv[4]
        
        pencil=scrollTo(driver, driver.find_element_by_xpath(path_to_pencil))
        pencil.click()
        while 1:
            time.sleep(5)
            availability=scrollTo(driver, driver.find_element_by_xpath(path_to_lesson))
            
            if availability.text != "Section Full":
                print("COURSE AVAILABLE! GO ENROLL NOW BEFORE IT IS TAKEN!!!!!")
            driver.refresh() #Refresh page
            time.sleep(5)
            pencil=driver.find_element_by_xpath(path_to_pencil)
            pencil.click()

    except Exception as e:
        print("Something went terribly wrong... Possible errors: Incorrect login, incorrect xpath's")
    