
class TestOrgManage:
    def test_add_group_success(self,get_index):
        group_list = get_index.go_to_my_page().go_to_organzation_manage().add_group("TestSelenium")
        assert "TestSelenium" in group_list

    def test_add_organzation_success(self,get_index):
        orgs_list = get_index.go_to_my_page().go_to_organzation_manage().add_organzation("testselenium")
        assert ('testselenium','TestSelenium',) in orgs_list

    def test_add_parts(self,get_index):
        part_list =  get_index.go_to_my_page().go_to_organzation_manage().add_part("test1")
        assert ('test1','testselenium') in part_list

    def test_add_member_success(self,get_index):
        users_list = get_index.go_to_my_page().go_to_organzation_manage().add_members('hybb','15283759307')
        assert ('testselenium','hybb') in  users_list
        assert ('TestSelenium全体','hybb') in users_list

