from selenium.webdriver.common.by import By

from test_homework_po.page.basepage import BasePage
from test_homework_po.page.contact_page import ContactPage


class Add_Member_Page(BasePage):
    _username = (By.ID,"username")
    _acctid = (By.ID,"memberAdd_acctid")
    _mail = (By.ID, "memberAdd_mail")
    def add_member(self,name,id,mail):
        self.find(*self._username).send_keys(name)
        self.find(*self._acctid).send_keys(id)
        self.find(*self._mail).send_keys(mail)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()

        return ContactPage(self.driver)