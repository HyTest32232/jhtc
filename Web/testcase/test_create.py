from Web.page_object.index_page import IndexPage

class TestCreateVideo:

    def test_create_video(self):
        index = IndexPage()
        phone_list = index.go_to_my_page().go_to_video_manage().create_get_video("test_selenium")
        assert "test_selenium" in phone_list