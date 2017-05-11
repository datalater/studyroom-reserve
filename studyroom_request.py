import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import getpass


class Reserver():

    def __init__(self):
        """사용자로부터 사용자로부터 고려대학교 포탈 id와 password를 입력받는다"""

        # self.user_id = input('ID를 입력하세요: ')
        self.user_id = 'kjs297'
        self.user_pwd = getpass.getpass('PWD를 입력하세요(Not echoing): ')


    def portal_login(self):
        """입력 받은 id와 pwd로 로그인한다"""
        ### 고려대학교 포탈에 GET방식으로 접속한다.

        print("(1/4) URL에 접속합니다...")
        portal_url = 'http://portal.korea.ac.kr/front/Intro.kpd'

        # self.driver = webdriver.Chrome(r'E:/Google_Drive/10학기취업/(30) JTCodingStudy/python/programs/studyroom-reserve/chromedriver.exe')
        self.driver = webdriver.Chrome(r'E:\Google_Drive\10학기취업\(30) JTCodingStudy\python\programs\studyroom-reserve\chromedriver.exe')
        self.driver.get(portal_url)

        ### 고려대학교 포탈에 LOGIN을 실시한다.

        print("(2/4) LOGIN을 실시합니다...")

        input_id = self.driver.find_element_by_xpath("//input[@id='oneid']")
        input_pwd = self.driver.find_element_by_name('pw')

        input_id.send_keys(self.user_id)
        input_pwd.send_keys(self.user_pwd)

        btn_login = self.driver.find_element_by_class_name('submit')
        ActionChains(self.driver).click(btn_login).perform()

    def infolife_click(self):
        ### 로그인 후 상단 바에 있는 정보생활 버튼을 클릭한다.

        print("(3/4) LOGIN이 완료되었습니다...")

        btn_infolife = self.driver.find_element_by_xpath("//a[contains(.,'정보생활')]")
        ActionChains(self.driver).click(btn_infolife).perform()

        ### 왼쪽 사이드 바에 있는 공간예약/관리를 클릭한다.

        delay = 2.5

        wait = WebDriverWait(self.driver, delay)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'm143')))

        btn_space1 = self.driver.find_element_by_xpath("//li[@id='m143']")
        ActionChains(self.driver).click(btn_space1).perform()

        ### 공간예약/관리의 하위 항목인 공간관리 및 예약신청을 클릭한다.

        btn_space2 = self.driver.find_element_by_xpath("//li[@id='sm1260']")
        ActionChains(self.driver).click(btn_space2).perform()

        print("(4/4) 공간예약/관리 페이지에 접속되었습니다...")

    def autosearch_click(self):

        time.sleep(3.5)

        print("(5/4) 자동검색 페이지에 접속되었습니다...")

        self.autosearch_url = 'http://cafm.korea.ac.kr/archibus/reserve_time.jsp'
        self.driver.get(self.autosearch_url)

        # print(self.driver.window_handles)
        # print(self.driver.current_window_handle)

        ### 첫번째 탭으로 focus를 바꾼다.

        self.driver.switch_to_window(self.driver.window_handles[0])

    def search(self):

        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Referer': 'http://cafm.korea.ac.kr/archibus/reserve_time.jsp'
        }

        params = {
        'em_check':0,
        'today_check':'2017-05-11',     # 오늘 날짜 (should be fixed)
        'bl_id':'011510',               # 현차관 (011510)
        'date':'2017-05-12',            # 예약 날짜
        'time_start':'19:00',           # 예약 시작시간
        'time_end':'22:00',             # 예약 끝시간
        }

        search_url = self.autosearch_url

        self.driver.post(search_url, params=params, headers=headers)

if __name__ == '__main__':
    ### 사용자로부터 고려대학교 포탈 id와 password를 입력받는다.

    reserver = Reserver()
    reserver.portal_login()
    reserver.infolife_click()
    reserver.autosearch_click()
    reserver.search()
