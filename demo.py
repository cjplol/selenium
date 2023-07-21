from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as sleep

class BilibiliTest:
    def __init__(self) :
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.bilibili.com/')
        sleep(2)
    
    def search(self):
        self.driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input').send_keys('clannad')
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[2]').click()
        sleep(3)
        #通过查找是否存在一个超链接“CLANNAD”，来进行搜索结果的断言
        try:
            #获取当前页的所有句柄
            num=self.driver.window_handles
            #切换到新的标签页
            self.driver.switch_to.window(str(num[1]))
            self.driver.find_element(By.LINK_TEXT,'CLANNAD')
            print("搜索断言：成功")
        except Exception as e:
            print(f"登录断言：失败，异常信息为{e}")

    def login(self):
        self.driver.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div[4]/div[2]/form/div[1]/input').send_keys('18218057842')
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div[4]/div[2]/form/div[3]/input').send_keys('cjp!98050505')
        sleep(5)

if __name__=='__main__':
    bili=BilibiliTest()
    #bili.search()
    bili.login()
