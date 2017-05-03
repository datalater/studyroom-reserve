import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass

user_id = input('ID를 입력하세요: ')
user_pwd = getpass.getpass('PWD를 입력하세요(Not echoing): ')

print("(1/4) URL에 접속합니다...")
portal_url = 'http://portal.korea.ac.kr/front/Intro.kpd'

driver = webdriver.Chrome('E:/Google_Drive/10학기취업/(30) jt_study/python/programs/chromedriver.exe')
driver.get(portal_url)

print("(2/4) LOGIN을 실시합니다...")

input_id = driver.find_element_by_xpath("//input[@id='oneid']")
input_pwd = driver.find_element_by_name('pw')

input_id.send_keys(user_id)
input_pwd.send_keys(user_pwd)

btn_login = driver.find_element_by_class_name('submit')
ActionChains(driver).click(btn_login).perform()

print("(3/4) LOGIN이 완료되었습니다...")

btn_infolife = driver.find_element_by_xpath("//a[contains(.,'정보생활')]")
ActionChains(driver).click(btn_infolife).perform()

btn_space1 = driver.find_element_by_xpath("//li[@id='m143')]")
ActionChains(driver).click(btn_space1).perform()

btn_space2 = driver.find_element_by_xpath("//li[@id='sm1260']")
ActionChains(driver).click(btn_space2).perform()

print("(4/4) 공간예약/관리 페이지에 접속되었습니다...")

search_url = "http://cafm.korea.ac.kr/archibus/reserve_time.jsp"
driver.get(search_url)
