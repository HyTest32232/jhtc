from time import sleep

from selenium.webdriver.common.by import By

from Web.page_object.base_page import BasePage


class OrganizationPage(BasePage):
    def add_members(self):
        #选择群组
        self.find(By.CSS_SELECTOR,'#form1 > div.formmiddle > div:nth-child(1) > div > div').click()
        sleep(1)
        self.find(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        #选择机构
        self.find(By.CSS_SELECTOR,'#form1 > div.formmiddle > div:nth-child(2) > div > div.el-input.el-input--suffix > span > span > i').click()
        sleep(1)
        self.find(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li').click()
        self.find(By.CSS_SELECTOR,'#form1 > div.formmiddle > div:nth-child(3) > div > input').send_keys("hybb")
        self.find(By.CSS_SELECTOR,"#form1 > div.formmiddle > div:nth-child(4) > div > input").send_keys("17388321779")
        self.find(By.CSS_SELECTOR,"#form1 > div.radioinfo > div.formbutton > button").click()
        sleep(1)
        return self.get_members()
    def get_members(self):
        self.find(By.CSS_SELECTOR,"#tab-2").click()
        groups = self.driver.find_elements(By.CSS_SELECTOR,"#pane-2 > div > div > p:nth-child(3)")
        users = self.driver.find_elements(By.CSS_SELECTOR,"#pane-2 > div > div > p:nth-child(2)")
        group_list = []
        user_list =[]
        for group in groups:
            group_list.append(group.text)
        for user in users:
            user_list.append(user.text)
        dict1 = zip(group_list,user_list)
        print(dict1)
        return dict1
