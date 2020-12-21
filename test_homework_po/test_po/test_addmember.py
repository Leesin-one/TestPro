import pytest

from test_homework_po.page.index_page import IndexPage


class TestAddMember_Po:
    @pytest.mark.parametrize("name,id,mail",[("wangwu1",1213231,"sas4ad@qq.com")])
    def test_index_login(self,name,id,mail):
        # name = "wangwuer"
        # id = 1123124
        # mail = "sasad@qq.com"
        self.main = IndexPage()
        name_list =self.main.goto_contact().click_add_member()\
            .add_member(name,id,mail).get_member()
        print(name_list)
        assert name in name_list




