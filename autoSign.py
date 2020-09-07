#_*_coding:utf-8_*_
import os
import requests
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

time.sleep(60)

driver = webdriver.Chrome()
url = 'https://uis.zafu.edu.cn/cas/login?service=http%3A%2F%2Fappui.zafu.edu.cn%2Fsso%2Flogin.jsp%3FtargetUrl%3D%7Bbase64%7DaHR0cDovL2FwcHVpLnphZnUuZWR1LmNuL2g1YXBwL3ZhcHBwYy9pbmRleC5odG0%2FYXBwPVlxZGpJbmRleCZmcm9tPW1lc3NhZ2UmaXNhcHBpbnN0YWxsZWQ9MA%3D%3D'
url2 = 'http://appui.zafu.edu.cn/h5app/vapppc/index.htm?app=YqdjIndex&from=message&isappinstalled=0'
username = ""
password = ""
decimal  = ''
province = ""
city     = ""
area     = ""

def work():
    # 获取用户信息
    def get_detail():
        global username
        global password
        global decimal
        global province
        global area
        global city
        path = os.getcwd()+"/detail/account1.txt"
        with open(path, "r", encoding = "utf-8") as f:
            username = f.readline().splitlines()
            password = f.readline().splitlines()
            decimal  = f.readline().splitlines()
            province = f.readline().splitlines()
            city     = f.readline().splitlines()
            area     = f.readline().splitlines()

    # 登录 以及框架切换
    def signin(username, password):
        global url
        global driver
        driver.get(url)
        time.sleep(1)

        driver.find_element_by_id('username').click()
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').click()
        driver.find_element_by_id('password').send_keys(password)
        #driver.find_element_by_id('login_button').click()
        driver.find_element_by_xpath("//input[@type='submit' and @value='登 录']").click()
        time.sleep(3)

        # 框架切换
        #driver.find_element_by_xpath("//*[@id='curareaname']").click()
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to_frame(iframe)

        driver.find_element_by_id('curareaname').click()

    # 填写province, city, area
    def PCA(province, city, area):
        global driver
        time.sleep(2)
        j = 1
        l = province + city + area
        # 依次填写省,市,区
        for compare in l:
            flag = 1
            i = 1
            while flag:
                text = driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div["+str(j)+"]/ul/li["+str(i)+"]").text
                driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div["+str(j)+"]/ul/li["+str(i)+"]").click()            
                time.sleep(0.5)
                print(text)
                if (text == compare):
                    flag = 0
                i = int(i)
                i += 1
            j += 1
            time.sleep(1)
        driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[1]/button[2]").click()

    # 其他信息填写
    def others(decimal):
        
        # 绿码确认
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[20]/div[2]/div/input").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[1]/button[2]").click()

        # 体温
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[11]/div[2]/div/input").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[11]/div[2]/div/input").send_keys(decimal)

        # 各种否
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[22]/div/div/div[2]/div/i").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[24]/div/div/div[2]").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[26]/div/div/i").click() 
        
        # 确认
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/button").click() 


    get_detail()
    signin(username, password)
    PCA(province, city, area)
    others(decimal=''.join(decimal))
    
def WORK():
    def time_dist():
        cur_hour = datetime.datetime.now().hour
        cur_min  = datetime.datetime.now().minute
        cur_sec  =  datetime.datetime.now().second
        total = int(cur_hour) * 60 * 60 + cur_min * 60 + cur_sec
        dist = 86400 - total
        return dist

    def time_control():
        work()
        global driver
        driver.close()
        driver.quit()
        while(1):
            time.sleep(time_dist() + 10)
            driver = webdriver.Chrome()
            work()
            driver.close()
            driver.quit()
    
    time_control()

WORK()
