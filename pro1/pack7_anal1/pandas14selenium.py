#이클립스 또는 jupyter notebook 등의 편집기에서 실행해 보기 실습 예 : 화면 캡처

from selenium import webdriver

try:
    url = "https://www.daum.net"
    browser = webdriver.Chrome('C:/work/chromedriver')
    browser.implicitly_wait(3)

    browser.get(url);
    browser.save_screenshot("다음_img.png")
    browser.quit()

    print('성공')

except Exception:
    print('에러')