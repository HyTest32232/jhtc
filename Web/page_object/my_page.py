from selenium.webdriver.common.by import By
from Web.page_object.base_page import BasePage
from Web.page_object.video_manage_page import VideoPage


class MyPage(BasePage):
    def go_to_video_manage(self):
        self.find(By.CSS_SELECTOR,'#app > div > div:nth-child(2) > div > div.left > div > div.barlist > div:nth-child(4)').click()
        return VideoPage(self.driver)
