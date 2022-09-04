from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    _base_url = ""
    def __init__(self,base_driver:WebDriver=None,):
        if base_driver == None:
            chrome_options = Options()
            chrome_options.add_argument("headless")
            chrome_options.add_argument("no-sandbox")
            chrome_options.add_argument('disable-dev-shm-usage')
            chrome_options.add_argument("disable-gpu")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self.driver.find_element(By.XPATH, '//*[@id="register"]/form/div[1]/div/div/input').send_keys("17388321779")
            self.driver.find_element(By.XPATH, '//*[@id="register"]/form/div[2]/div/div/input').send_keys("huyue123")
            self.driver.find_element(By.XPATH, '//*[@id="register"]/form/div[3]/div/button').click()
        else:
            self.driver = base_driver
            self.driver.implicitly_wait(2)

    def find(self,by,locator=None):
        """
        封装查找操作
        :return:
        """
        if locator == None:
            web_ele = self.driver.find_element(*by)
        else:
            web_ele = self.driver.find_element(by=by,value=locator)
        print(f'查找到元素为{web_ele}')
        return web_ele
