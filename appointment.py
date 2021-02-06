# -*- coding: UTF-8 -*-
# Author: kane

from selenium import webdriver
from time import sleep
import mp3play





from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# driver.get('https://wy.guahao.com/expert/book/3034da78-049c-43e7-aeff-e4932405cea1000?hospitalId=8f113a19-eee7-47b8-9517-2ad069a2f57a000&hospDeptId=ea5c22c3-47e4-44c7-b4a7-de9e0f9f48e9000#')
driver.get('https://wy.guahao.com/expert/book/8a1f07c9-76c6-46a1-a60a-efb0802d85e8000?hospitalId=8f113a19-eee7-47b8-9517-2ad069a2f57a000&hospDeptId=ea5c22c3-47e4-44c7-b4a7-de9e0f9f48e9000#')


def fetch():
    try:
        platform_elements = driver.find_elements_by_css_selector("ul[class='cpt-book-workspace--shift-item']>li")
    except NoSuchElementException as e:
        print(e)
        return
    if not platform_elements:
        print(f"none result {platform_elements}")
        return
    for platform_element in platform_elements:
        content = platform_element.text
        if content.endswith("预约"):
            print("开始预约了")
            mp3play.load("261204262634929.mp3").play()
    driver.refresh()


if __name__ == '__main__':
    while True:
        fetch()
        sleep(30)
