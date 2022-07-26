from Web.page_object.index_page import IndexPage

class TestCreateVideo:
    index = IndexPage()
    def test_add_group(self):
        group_list = self.index.go_to_my_page().go_to_organzation_manage().add_group("TestSelenium")
        assert "TestSelenium" in group_list

    def test_add_organzation(self):
        orgs_list = self.index.go_to_my_page().go_to_organzation_manage().add_organzation("testselenium")
        assert ('testselenium','TestSelenium',) in orgs_list

    def test_add_member(self):
        users_list = self.index.go_to_my_page().go_to_organzation_manage().add_members('hybb','15283759307')
        assert ('testselenium','hybb') in  users_list
        assert ('TestSelenium全体','hybb') in users_list

    def test_create_video(self):
        phone_list = self.index.go_to_my_page().go_to_video_manage().create_get_video("test_selenium")
        assert "test_selenium" in phone_list

