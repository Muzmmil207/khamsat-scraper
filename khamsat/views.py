from time import sleep

from bs4 import BeautifulSoup
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from web_scraper.settings import BASE_DIR


def data():
    browser = webdriver.Chrome(BASE_DIR  / 'chromedriver.exe')
    community_requests = []

    browser.implicitly_wait(30)
    browser.get('https://khamsat.com/community/requests')
    # sleep(2)
    b = browser.find_element(By.ID, 'community_loadmore_btn')
    # b.send_keys(Keys.ENTER)
    browser.execute_script('arguments[0].click()', b)
    sleep(0.5)
    browser.execute_script('arguments[0].click()', b)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    requests_table_body = soup.find('tbody')

    request_details = requests_table_body.find_all('td',  class_="details-td")
    for details in request_details:
        dic = {}
        dic['request_title'] = details.find('a', class_="ajaxbtn").text.strip()
        # dic['request_url'] =  details.find('a', class_="ajaxbtn")["href"]
        # dic['request_user'] = details.find('a', class_="user").text.strip()
        # dic['request_since'] = details.find('span').text.strip()
        community_requests.append(dic)

    return community_requests

def scraper(request):
    data_ = data()
    return render(request, "main.html", {'d':data_})




