import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

url = ""
browser = webdriver.Chrome(options=options) 
browser.get(url)
browser.maximize_window()

usr = ""
pwd = ""

# in case of alert modal
def alert():

    try:
        browser.find_element_by_xpath("").click()

    except:
        pass


def log_in():

    # pulldown select
    browser.find_element_by_xpath("").click()

    # id
    id = browser.find_element_by_xpath("")
    id.send_keys(usr)

    # pw
    pw = browser.find_element_by_xpath("")
    pw.send_keys(pwd)

    # sign in
    browser.find_element_by_xpath("").click()
    time.sleep(1)

    # dashboard
    browser.find_element_by_xpath("").click()
    alert()

    # item
    browser.find_element_by_xpath("").click()
    time.sleep(1)
    alert()


def category1():

    browser.find_element_by_xpath("").click()
    time.sleep(1)
    alert()

    soup = BeautifulSoup(browser.page_source, "lxml")
    item0 = soup.find("span", attrs={"id":"item_0"}).get_text()
    item1 = soup.find("span", attrs={"id":"item_1"}).get_text()
    item2 = soup.find("span", attrs={"id":"item_2"}).get_text()
    disable = soup.find("span", attrs={"class":"disable_item"}).get_text()

    with open("item.txt", "w", encoding="utf8") as f:
        f.write("----------Category1----------")
        f.write(f"\n{item0.strip()}")
        f.write(f"\n{item1.strip()}")
        f.write(f"\n{item2.strip()}")
        f.write(f"\ndisable: {disable.strip()}")


def category2():

    browser.find_element_by_xpath("").click()
    time.sleep(1)
    alert()

    soup = BeautifulSoup(browser.page_source, "lxml")
    item0 = soup.find("span", attrs={"id":"item_0"}).get_text()
    item1 = soup.find("span", attrs={"id":"item_1"}).get_text()
    disable = soup.find("span", attrs={"class":"disable_item"}).get_text()

    with open("jp.txt", "a", encoding="utf8") as f:
        f.write("\n----------Category2----------")
        f.write(f"\n{item0.strip()}")
        f.write(f"\n{item1.strip()}")
        f.write(f"\ndisable: {disable.strip()}")
        

if __name__ == "__main__":
    log_in()
    category1()
    category2()


browser.quit()
