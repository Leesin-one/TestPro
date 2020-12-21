from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_homework_po.page.basepage import BasePage


class ContactPage(BasePage):
    def click_add_member(self):
        from test_homework_po.page.addmember_page import Add_Member_Page
        ele = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        # WebDriverWait注意要添加的是元组类型
        self.wait(ele,10)
        while True:
            self.driver.find_element(*ele).click()
            username = self.finds(By.ID,"username")
            if len(username) > 0:
                break
        return Add_Member_Page(self.driver)
    # 断言
    def get_member(self):
        sleep(2)
        titles = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in titles:
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        return name_list
