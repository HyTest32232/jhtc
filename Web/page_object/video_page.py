from time import sleep
from selenium.webdriver.common.by import By
from Web.page_object.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class VideoPage(BasePage):
        _username_locator = (By.CSS_SELECTOR,"#form > div.formmiddle > div:nth-child(2) > div > input")

        def create_get_video(self,name):
            self.find(By.ID, "tab-1").click()
            self.find(By.ID, "upload").send_keys("D:\工作\code\data\国家重点·公办院校.mp4")
            sleep(1)
            self.find(self._username_locator).send_keys(name)
            # 选择群组Test1
            self.driver.execute_script('document.querySelector("#form > div.formmiddle > div:nth-child(3) > div > div > input").click()')
            sleep(1)
            self.find(By.CSS_SELECTOR,'body>div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(6)').click()
            # 选择机构test_1
            self.driver.execute_script('document.querySelector("#form > div.formmiddle > div:nth-child(4) > div > div>input").click()')
            sleep(1)
            self.driver.execute_script('document.querySelector("body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()')
            # 选择栏目公告栏
            self.find(By.CSS_SELECTOR,"#form > div.formmiddle > div:nth-child(5) > div > div > input").click()
            sleep(1)
            self.driver.execute_script('document.querySelector("body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()')
            # 提交
            self.find(By.CSS_SELECTOR, "#form > div.radioinfo > div.formbutton > button").click()
            #查询是否创建成功
            while True:
                sleep(3)
                try:
                    self.find(By.XPATH,"/html/body/div[3]/p").is_displayed()
                    break
                except Exception as e:
                    print('视频上传中')
            self.find(By.ID, "tab-2").click()
            eles = self.driver.find_elements(By.CSS_SELECTOR, "#pane-2 > div > div.el-row > div.memberbox > div.memberbox-right p:nth-child(1)")
            phone_list = []
            for ele in eles:
                phone_list.append(ele.text)
            return phone_list