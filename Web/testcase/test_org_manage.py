from selenium import webdriver
from Web.page_object.index_page import IndexPage
import pytest

class TestOrgManage:

    @pytest.mark.run(order=1)
    def test_add_group(self,get_index):
        group_list = get_index.go_to_my_page().go_to_organzation_manage().add_group("TestSelenium")
        assert "TestSelenium" in group_list

    @pytest.mark.run(order=2)
    def test_add_organzation(self,get_index):
        orgs_list = get_index.go_to_my_page().go_to_organzation_manage().add_organzation("testselenium")
        assert ('testselenium','TestSelenium',) in orgs_list

    @pytest.mark.run(order=3)
    def test_add_member(self,get_index):
        users_list = get_index.go_to_my_page().go_to_organzation_manage().add_members('hybb','15283759307')
        assert ('testselenium','hybb') in  users_list
        assert ('TestSelenium全体','hybb') in users_list
