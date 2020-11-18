from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.coursera.org/learn/understanding-visualization-data/lecture/KeSCz/what-is-statistics')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")

'''
#coding=utf-8                                                                                                                                                                              
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://pythonbasics.org'

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()
'''
