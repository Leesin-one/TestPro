from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver import TouchActions

def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    opt.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    # 存入cookie
    cookies = driver.get_cookies()
    print(driver.get_cookies())
    with open("add_member.yml", "w", encoding="UTF-8") as f:
        yaml.dump(cookies, f)

class Test_Add_Member():
    def setup(self):
        self.driver = webdriver.Chrome()
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("add_member.yml") as f:
            get_cookies=yaml.safe_load(f)
        print(get_cookies)
        for cookie in get_cookies:
             self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击通讯录按钮
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
        # 点击添加成员按钮
        # self.driver.find_element_by_xpath('//*[@id="js_contacts47"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        # self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn js_add_member'][1]").click()
        self.driver.find_element_by_link_text("添加成员").click()
        sleep(2)
        # 添加用户名
        add_name = self.driver.find_element_by_id("username")
        add_name.send_keys("aaa")
        sleep(2)
        # 添加账号
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("1365153364")
        sleep(2)
        # 添加手机号
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15678923451")
        sleep(2)
        # 滑动到底端
        action = TouchActions(self.driver)
        action.scroll_from_element(add_name,0,10000)
        action.perform()
        sleep(2)
        # 点击保存按钮
        self.driver.find_element_by_link_text("保存").click()








    # def test_add_member(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
    #     self.driver.find_element_by_id("username").send_keys("curry")
    #     self.driver.find_element_by_id("memberAdd_acctid").send_keys("136515336")
    #     self.driver.find_element_by_xpath('//*[@id="js_contacts75"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()