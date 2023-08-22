# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:15:46 2021

@author: Dias
"""


#%%

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


#%%

def credenciais():        
    data = pd.read_csv("reddit_passes.csv", sep =";")
    list_user = list(data["username"])
    list_pass = list(data["password"])
    
    for user, passa in zip (list_user, list_pass):
        iniciar(user,passa)

    
def iniciar(username,password):

    website = "https://old.reddit.com/"
    driver = webdriver.Chrome("C:\\Webdrivers\\chromedriver.exe")
    driver.get(website)
    
    ##################login with credentials
    #type in username
    
    usrnm = driver.find_element_by_name("user")
    usrnm.clear()
    usrnm.send_keys(username)
    
    #type in password
    pas = driver.find_element_by_name("passwd")
    pas.clear()
    pas.send_keys(password)
    driver.implicitly_wait(1)
    pas.send_keys(Keys.RETURN)
    
    
    
    ################wait to authenticate
    sleep(3)
    
    #the user page should be the following format https://old.reddit.com/user/XXXXX/
    #replace XXXXX with the username with the post that should be upvoted.
    user_page = ""
    driver.get(user_page)
    

    #change the xpath to the post that is supposed to be upvoted (or downvoted)
    post_upvote = '//*[@id="thing_t3_oequfb"]/div[1]/div[1]'
    
  
    upvote = driver.find_element_by_xpath(post_upvote)
    
    upvote.click()
    
    driver.close()

credenciais()








































