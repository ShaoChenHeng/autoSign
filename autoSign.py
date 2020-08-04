#_*_coding:utf-8_*_
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

time.sleep(60)
username = ""
password = ""
url = 'https://uis.zafu.edu.cn/cas/login?service=http%3A%2F%2Fappui.zafu.edu.cn%2Fsso%2Flogin.jsp%3FtargetUrl%3D%7Bbase64%7DaHR0cDovL2FwcHVpLnphZnUuZWR1LmNuL2g1YXBwL3ZhcHBwYy9pbmRleC5odG0%2FYXBwPVlxZGpJbmRleCZmcm9tPW1lc3NhZ2UmaXNhcHBpbnN0YWxsZWQ9MA%3D%3D'
url2 = 'http://appui.zafu.edu.cn/h5app/vapppc/index.htm?app=YqdjIndex&from=message&isappinstalled=0'
decimal = '36.5'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

#登录
driver.find_element_by_id('username').click()
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').click()
driver.find_element_by_id('password').send_keys(password)
#driver.find_element_by_id('login_button').click()
driver.find_element_by_xpath("//input[@type='submit' and @value='登 录']").click()
time.sleep(3)

#driver.find_element_by_xpath("//*[@id='curareaname']").click()
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)

driver.find_element_by_id('curareaname').click()
#省
time.sleep(2)
for i in range(1,12):
    driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[1]/ul/li["+str(i)+"]").click()
    time.sleep(0.5)

#time.sleep(3)
#市
time.sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[2]/ul/li[2]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[2]/ul/li[1]").click()

#区
time.sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[3]/ul/li[2]").click()
time.sleep(0.5)
for j in range(3,11):
    driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[3]/ul/li["+str(j)+"]").click()
    time.sleep(0.5)


driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[1]/button[2]").click()





driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[20]/div[2]/div/input").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[2]/div[1]/ul/li[1]").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[1]/button[2]").click()

#体温
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[11]/div[2]/div/input").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[11]/div[2]/div/input").send_keys(decimal)

#各种否
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[22]/div/div/div[2]/div/i").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[24]/div/div/div[2]").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[26]/div/div/i").click() 

time.sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/button").click() 
