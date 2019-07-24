# cookie = {
#     'UM_distinctid':'16bee6b6248a98-0967d1ecca1413-e343166-15f900-16bee6b6249bc3',
#     '_uab_collina':'156307314451508902911282',
#     'acw_tc':'6f1a9e4615630731477555861efb1d812d1403c182661e3f463736a3ab',
#     'QCCSESSID':'tmv33f0a515gv6glkk631rk4v7',
#     'hasShow':'1',
#     'Hm_lvt_3456bee468c83cc63fb5147f119f1075':'1563073144,1563075251,1563160077,1563179574',
#     'CNZZDATA1254842228':'600613408-1563068738-https%253A%252F%252Fwww.baidu.com%252F%7C1563178451',
#     'Hm_lpvt_3456bee468c83cc63fb5147f119f1075':'1563181215',
#     'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f':'%7B%22sid%22%3A%201563179305257%2C%22updated%22%3A%201563181256437%2C%22info%22%3A%201563073142792%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%221208c92224e0779acff7f371ab1ffd3c%22%7D'
# }

cookie = 'QCCSESSID=68cddskba3m0md5v3d0cq57so4; zg_did=%7B%22did%22%3A%20%2216bf513b3b77aa-0c8fcb19fce5ab-e343166-1fa400-16bf513b3b8427%22%7D; UM_distinctid=16bf513b411193-065de84ff11e65-e343166-1fa400-16bf513b4128e9; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1563184838; _uab_collina=156318483780507031507826; acw_tc=6f306a1c15631848397475006ec8698007a1dd0fff7c3c7d4e7070e026; hasShow=1; CNZZDATA1254842228=817120214-1563179532-%7C1563237421; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1563238113; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201563236699318%2C%22updated%22%3A%201563238204823%2C%22info%22%3A%201563184837569%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%221208c92224e0779acff7f371ab1ffd3c%22%7D'

from selenium import webdriver
from selenium.webdriver.common.by import By # 定位
from selenium.webdriver.support.ui import WebDriverWait #显性等待库
import time
from selenium.webdriver.common.action_chains import ActionChains
import random


chromeOptions = webdriver.ChromeOptions()
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
chromeOptions.add_argument('user-agent=%s'%user_agent)
chromeOptions.add_argument('--user-data-dir=C:/Users/dell/AppData/Local/Google/Chrome/User Data')
driver = webdriver.Chrome(chrome_options = chromeOptions)

bbs_url='https://www.qichacha.com/user_login?back=%2F'
def cookie_login(bbs_url, account='15691850605', password='123456'):
    driver.delete_all_cookies()
    '''通过request 登陆系统，获取cookie'''
    driver.get(bbs_url)
    driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
    driver.find_element_by_xpath('//*[@id="nameNormal"]').click()
    driver.find_element_by_xpath('//*[@id="nameNormal"]').send_keys(account)

    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pwdNormal"]').click()
    driver.find_element_by_xpath('//*[@id="pwdNormal"]').send_keys(password)
    #
    # time.sleep(0.5)
    # target = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
    # actions = ActionChains(driver)
    # actions.click_and_hold(target).perform()
    # # actions.drag_and_drop_by_offset(target,310,0).perform()
    #
    # # actions.click_and_hold(target).move_by_offset(0,100).move_by_offset(0,110).move_by_offset(0,120).release()
    #
    # maxInt = 310
    # while True:
    #     x = random.randint(5, 50)
    #     actions.move_by_offset(x,0).perform()
    #     maxInt -= x
    #     if maxInt<0:
    #         break
    #     time.sleep(0.05)
    # actions.release().perform()

    print('拖住完成')
    time.sleep(2)

    # driver.find_element_by_xpath('//*[@id="user_login_normal"]/button').click()
    # cookies = driver.get_cookies()
    # time.sleep(5)
    # print(cookies)
    # for cookie_one in cookies:
    #     print(cookie_one)
cookie_login(bbs_url)