# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:05:55 2019

@author: dell
"""

import numpy as np ,pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging
import requests
import random
# from ua import agents
# from cookie import cookie



def get_new_url(name):
    root_url='https://www.qichacha.com/'
    chromeOptions = webdriver.ChromeOptions()
    # 设置代理
    # chromeOptions.add_argument("--proxy-server=http://121.233.207.225:9999")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    user_data = 'C:/Users/dell/AppData/Local/Google/Chrome/User Data'  #这里面填你的user data对应的文件夹
    # user_agent = random.choice(agents)
    chromeOptions.add_argument('user-agent=%s'%user_agent)
    chromeOptions.add_argument('--user-data-dir=%s'%user_data)
    # chromeOptions.add_argument('Cookie=%s'% cookie)
    browser = webdriver.Chrome(chrome_options = chromeOptions)

    # browser.add_cookie({'name':'hasShow','value':'1'})
    # browser.add_cookie({'name': 'acw_tc', 'value': '6f306a1c15631848397475006ec8698007a1dd0fff7c3c7d4e7070e026'})
    # browser.add_cookie({'name': '_uab_collina', 'value': '156318483780507031507826'})
    # browser.add_cookie({'name': 'CNZZDATA1254842228', 'value': '817120214-1563179532-%7C1563179532'})
    browser.get(root_url)

    time.sleep(1.5)
    try:
        browser.find_element_by_xpath('//*[@id="searchkey"]').click()
        time.sleep(1.5)
        browser.find_element_by_id("searchkey").clear()
        browser.find_element_by_id("searchkey").send_keys(name)
        browser.find_element_by_id("searchkey").send_keys(Keys.ENTER)
        url_Combin = browser.find_element_by_xpath('//*[@id="search-result"]/tr[1]/td[3]/a').get_property('href')
        # print(b)
        browser.get(url_Combin)
        MainName = browser.find_element_by_xpath('//*[@id="company-top"]/div[2]/div[2]/div[1]/h1').text
        location = browser.find_element_by_xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[7]/td[2]').text
        jg = browser.find_element_by_xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[6]/td[4]').text
    except:
        logging.info('Can not find the result of %s'% name)
        browser.quit()
        return None

    browser.quit()
    return {'url':url_Combin,'l':location,'jg':jg,'MainName':MainName}

fileName = '数据样本.xlsx'   #需要处理的文件名
fileSave = 'results.txt'   #保存结果的文件名
import sys
#sys.path.insert(0,r'C:\Users\dell\AppData\Local\Google\Chrome\Application') #不同电脑Chrome浏览器位置不同！

def save(content):
    with open(fileSave,'a+') as f:
        f.write(content[0]+'\t'+content[1]+'\t'+content[2]+'\t'+content[3]+'\t'+content[4]+'\n')

if __name__ == '__main__':
    dataPD = pd.read_excel(fileName,sheet_name='Sheet1')
    names = list(dataPD['被参控公司'].values)
    nameToURL = {}
    for name in names:
        results =get_new_url(name)
        if results != None:
            nameToURL[name]=results
            save([name,results['MainName'],results['url'],results['l'],results['jg']])
        else:
            nameToURL[name] = -1
            save([name,'-1','-1','-1','-1' ])
