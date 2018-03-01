from selenium import webdriver
from urllib.error import HTTPError
import time
from selenium.common.exceptions import NoSuchElementException

url='https://www.amazon.in/'
driver=webdriver.Chrome()
driver.get(url)
category=driver.find_element_by_xpath('//*[@id="nav-link-shopall"]').click()
time.sleep(0.2)
x='//*[@id="shopAllLinks"]/tbody/tr/td[2]/div[2]/ul/li[2]/a'
bakchodi=x.split('li[2]')
product_links=[]
for i in range(2,5):
    new_x=bakchodi[0] + 'li[' + str(i) + ']' + bakchodi[1]
    mens_fashion=driver.find_element_by_xpath(new_x).click()
    j=1
    xpath='//*[@id="result_i"]/div/div[3]/div[1]/a'
    new_xpath=xpath.split('_i')
    while(j<3):
        print(j)
        d=[]
        b=driver.find_elements_by_tag_name('li')
        # print(len(b))
        for i in range(0,len(b)):
            c=b[i].get_attribute('id')
            if c!='':
                e=c.split('result_')
                d.append(int(e[1]))
        print(d)
        for i in range(d[0],d[-1]):
            abc=new_xpath[0] + '_' + str(i) + new_xpath[1]
            try:
                link=driver.find_element_by_xpath(abc).get_attribute('href')
                product_links.append(link)
                print(link)
            except(NoSuchElementException):
                print('Sponsored Link')
        j+=1
        print(len(product_links))
        next_page = driver.find_element_by_xpath('//*[@id="pagnNextString"]')
        driver.execute_script('arguments[0].click();', next_page)
        time.sleep(6)
    print('\n')
    print('Catergory 1 over')
    print('\n')
    driver.get('https://www.amazon.in/gp/site-directory/ref=nav_shopall_btn/260-5666397-1854820')
    time.sleep(2)
