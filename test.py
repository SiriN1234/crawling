from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

#경로
url = 'C:\\chatbot\\'
driver = webdriver.Chrome(url + 'chromedriver.exe')
oneroomURL = 'https://realty.daum.net/home/oneroom/map'
driver.get(oneroomURL)

# 다음 부동산 원룸 페이지에서 용산역 검색
driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/input').send_keys('용산역')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/button').click()
driver.implicitly_wait(1) # 1초 대기

page = driver.page_source

# 월세 리스트 담을 빈 리스트 생성
total_lst = []

info = bs(page, 'lxml')

div = info.find("div", class_ = "css-1dbjc4n r-13awgt0 r-eqz5dr r-1777fci")

lst = []

for a in div :
    lst.append(a.get_text())
    
print(lst)
