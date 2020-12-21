from test_homework_po.page.basepage import BasePage
from test_homework_po.page.contact_page import ContactPage


class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        return ContactPage(self.driver)
