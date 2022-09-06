import configparser
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    _base_url = ""
    def __init__(self,base_driver:WebDriver=None):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['USERPROFILE'],'iselenium.ini'))
        chrome_options = Options()
        chrome_options.add_argument("no-sandbox")
        chrome_options.add_argument("disable-gpu")
        if base_driver == None:

            try:
                broswer = os.environ["broswer"]
            except KeyError:
                broswer = None
            # 无头模式
            if broswer is not None and broswer.lower() == 'no_gui':
                chrome_options.add_argument('headless')
                self.driver = webdriver.Chrome(options=chrome_options)
            #hub模式
            elif broswer is not None and broswer.lower() == 'remote':
                docker_remote = config.get('driver','remote')
                self.driver = webdriver.Remote(command_executor=docker_remote,desired_capabilities=DesiredCapabilities.CHROME)
            else:
                self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            self.driver.find_element(By.XPATH, '//*[@id="register"]/form/div[1]/div/div/input').send_keys("17388321779")
            self.driver.find_element(By.XPATH, '//*[@id="register"]/form/div[2]/div/div/input').send_keys("huyue123")
            self.driver.find_element(By.XPATH, '//*[@id="register"]/form/div[3]/div/button').click()
        else:
            self.driver = base_driver

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

    def close(self):
        sleep(3)
        self.driver.quit()
