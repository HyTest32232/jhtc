import allure

from Web.page_object.index_page import IndexPage


@allure.feature("机构管理")
class TestOrgManage:
    def setup(self):
        self.index = IndexPage()
    def teardown(self):
        self.index.close()
    @allure.story("添加群组成功")
    def test_add_group_success(self):
        group_list = self.index.go_to_my_page().go_to_organzation_manage().add_group("TestSelenium")
        assert "TestSelenium" in group_list
    @allure.story("添加机构成功")
    def test_add_organzation_success(self):
        orgs_list = self.index.go_to_my_page().go_to_organzation_manage().add_organzation("testselenium")
        assert ('testselenium','TestSelenium') in orgs_list
    @allure.story("添加栏目成功")
    def test_add_parts_success(self):
        part_list =  self.index.go_to_my_page().go_to_organzation_manage().add_part("test1")
        assert ('test1','testselenium') in part_list
    @allure.story("添加成员成功")
    def test_add_member_success(self):
        users_list = self.index.go_to_my_page().go_to_organzation_manage().add_members('hybb','15283759307')
        assert ('testselenium','hybb') in  users_list
        assert ('TestSelenium全体','hybb') in users_list


