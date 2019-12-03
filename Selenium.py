from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('D:\chromedriver')

browser.get('https://selenium.dev/')
browser.implicitly_wait(20)

#Searching for Downloads and click on it
downloads = browser.find_element_by_link_text('Downloads')
downloads.text
downloads.get_attribute('href')
downloads.click()

#Searching for Projects and click on it
projects = browser.find_element_by_link_text('Projects')
projects.click()

#Looking for Search Bar and input a text
searchBar = browser.find_element_by_id('gsc-i-id1')
searchBar.send_keys('downloads')
searchBar.send_keys(Keys.ENTER)