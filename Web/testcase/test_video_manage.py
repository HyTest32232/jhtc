from Web.page_object.index_page import IndexPage

class TestVideoManage:
    def test_create_video_success(self,get_index):
        phone_list = get_index.go_to_my_page().go_to_video_manage().create_get_video("test_selenium")
        assert "test_selenium" in phone_list
