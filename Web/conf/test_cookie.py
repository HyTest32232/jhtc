from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookie:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://www.netimedia.cn/#/login")
        self.driver.find_element(By.XPATH,'//*[@id="register"]/form/div[1]/div/div/input').send_keys("17388321779")
        self.driver.find_element(By.XPATH,'//*[@id="register"]/form/div[2]/div/div/input').send_keys("huyue123")
        self.driver.find_element(By.XPATH,'//*[@id="register"]/form/div[3]/div/button').click()
        cookies = self.driver.get_cookies()
        with open("../../data/cookies.yaml", "w", encoding="utf-8")as f:
            yaml.safe_dump(cookies,f)

    def test_add_cookie(self):
        self.driver.get("https://www.netimedia.cn/#/login")
        cookies = yaml.safe_load(open("../../data/cookies.yaml"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(5)
        self.driver.get("http://www.netimedia.cn/#/index")
