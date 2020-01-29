#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#те кто говорят что селениум глюченный тот просто плохой программист... (c) big-vl
#я очень долго работаю с этим модулем и драйвером, я хочу от сообщества 
#гитхаб что бы развивали мой код и в дальнейшем...
#those who say that selenium is buggy is just a bad programmer...  (c) big-vl
#I have been working with this module and driver for a very long time, I want the 
#github community to develop my code in the future...


from selenium import webdriver
#i am use google chrome, my practic 100 000 page parse
from selenium.webdriver.chrome.options import Options

#i am work very good use selenium, this is nice code next programming
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException

#function

def isDisplayed():
    try:
        browser.find_element_by_xpath("//*[text()='find text vwhis in page']")
    except NoSuchElementException:
        return False
    return True
#use function

if (isDisplayed() == True):
    print('text find, pleas replace hash tag or replace xpatch')
else:
    print('not found text, my style php/python *smile*')
