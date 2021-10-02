from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def authorization(login_, password_):

    driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    driver.get('https://passport.yandex.ru/auth/')
    login = driver.find_element_by_name('login')
    time.sleep(2)
    login.send_keys(login_)
    login.send_keys(Keys.RETURN)
    time.sleep(2)
    password = driver.find_element_by_id('passp-field-passwd')
    password.send_keys(password_)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.close()


if __name__ == '__main__':
    authorization(input('Введите логин: '), input('Введите пароль: '))
