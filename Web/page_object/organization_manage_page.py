from time import sleep
from selenium.webdriver.common.by import By
from Web.page_object.base_page import BasePage

class OrganizationPage(BasePage):

    def add_group(self,name):
        """
        添加群组
        :return:
        """
        self.find(By.CSS_SELECTOR,"#tab-3").click()
        self.find(By.CSS_SELECTOR,"#form2 > div.formmiddle > div:nth-child(1) > div > input").send_keys(name)
        self.find(By.CSS_SELECTOR,'#form2 > div.radioinfo > div.formbutton > button').click()
        sleep(1)
        return self.get_group()

    def get_group(self):
        """
        获取群组
        :return:
        """
        self.find(By.CSS_SELECTOR,"#tab-4").click()
        groups = self.driver.find_elements(By.CSS_SELECTOR,"#pane-4 > div.groupmanage > div >p:nth-child(1)")
        group_list = []
        for group in groups:
            group_list.append(group.text)
        return group_list

    def add_organzation(self,name):
        """
        创建机构
        :param name:
        :return:
        """
        self.find(By.CSS_SELECTOR,'#tab-5').click()
        self.driver.implicitly_wait(3)
        self.find(By.ID,"upload").send_keys(r'D:\工作\code\data\1.jpg')
        sleep(2)
        self.find(By.CSS_SELECTOR,"#form3 > div.formmiddle > div:nth-child(1) > div > div").click()
        sleep(2)
        self.find(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:first-child').click()
        sleep(1)
        self.find(By.CSS_SELECTOR,"#form3 > div.formmiddle > div:nth-child(2) > div > input").send_keys(name)
        self.find(By.CSS_SELECTOR,"#form3 > div.radioinfo > div.formbutton > button").click()
        while True:
            sleep(2)
            try:
                self.find(By.CSS_SELECTOR,"body > div.el-message.el-message--success").is_displayed()
                break
            except Exception as e:
                print("加载中")
        return self.get_organzation()

    def get_organzation(self):
        """
        获取机构
        :return:
        """
        self.find(By.ID,"tab-6").click()
        org_list = []
        group_list = []
        orgs = self.driver.find_elements(By.CSS_SELECTOR,"#pane-6 > div.manageOrgan > div.memberManage_box > div > div.memberManage_text>p:nth-child(1)")
        groups = self.driver.find_elements(By.CSS_SELECTOR,"#pane-6 > div.manageOrgan > div.memberManage_box > div > div.memberManage_text > p:nth-child(3) > b")
        for org in orgs:
            org_list.append(org.text)
        for group in groups:
            group_list.append(group.text)
        orgs_list = list(zip(org_list,group_list))
        return orgs_list

    def add_members(self,name,phone):
        """
        添加成员
        :return:
        """
        #选择群组
        self.find(By.CSS_SELECTOR,'#form1 > div.formmiddle > div:nth-child(1) > div > div').click()
        sleep(1)
        self.find(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:last-child').click()
        #选择机构
        self.find(By.CSS_SELECTOR,'#form1 > div.formmiddle > div:nth-child(2) > div > div.el-input.el-input--suffix > span > span > i').click()
        sleep(1)
        self.find(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:first-child').click()
        self.find(By.CSS_SELECTOR,'#form1 > div.formmiddle > div:nth-child(3) > div > input').send_keys(name)
        self.find(By.CSS_SELECTOR,"#form1 > div.formmiddle > div:nth-child(4) > div > input").send_keys(phone)
        self.find(By.CSS_SELECTOR,"#form1 > div.radioinfo > div.formbutton > button").click()
        sleep(1)
        return self.get_members()
    def get_members(self):
        """
        获取成员
        :return:
        """
        self.find(By.CSS_SELECTOR,"#tab-2").click()
        groups = self.driver.find_elements(By.CSS_SELECTOR,"#pane-2 > div > div > p:nth-child(3)")
        users = self.driver.find_elements(By.CSS_SELECTOR,"#pane-2 > div > div > p:nth-child(2)")
        group_list = []
        user_list =[]
        for group in groups:
            group_list.append(group.text)
        for user in users:
            user_list.append(user.text)
        users_list = list(zip(group_list,user_list))
        return users_list