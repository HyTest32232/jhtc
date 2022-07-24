from selenium.webdriver.common.by import By

from Web.page_object.base_page import BasePage
from Web.page_object.my_page import MyPage
from Web.page_object.online_page import OnlinePage
from Web.page_object.video_page import VideoPage
from Web.page_object.serve_page import ServePage


class IndexPage(BasePage):
    _base_url = "https://www.netimedia.cn/#/login"
    def go_to_online_page(self):
        """
        跳转至直播页
        :return:
        """
        return OnlinePage()

    def go_to_video_page(self):
        """
        跳转至视频页
        :return:
        """
        self.find(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/ul/div[2]/li').click()
        return VideoPage()

    def go_to_serve_page(self):
        """
        跳转至服务页
        :return:
        """
        return ServePage()

    def go_to_my_page(self):
        """
        跳转至我的
        :return:
        """
        self.find(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/ul/div[5]').click()
        return MyPage(self.driver)