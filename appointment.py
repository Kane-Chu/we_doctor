# -*- coding: UTF-8 -*-
# Author: kane
import random
import time

from selenium import webdriver
from time import sleep
from playsound import playsound

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException

driver = webdriver.Chrome()

driver.get(
    'https://wy.guahao.com/expert/book/3034da78-049c-43e7-aeff-e4932405cea1000?hospitalId=8f113a19-eee7-47b8-9517-2ad069a2f57a000&hospDeptId=ea5c22c3-47e4-44c7-b4a7-de9e0f9f48e9000#')


# driver.get(
#     'https://wy.guahao.com/expert/book/8a1f07c9-76c6-46a1-a60a-efb0802d85e8000?hospitalId=8f113a19-eee7-47b8-9517-2ad069a2f57a000&hospDeptId=ea5c22c3-47e4-44c7-b4a7-de9e0f9f48e9000#')


def fetch():
    try:
        # 点击确定 取消遮盖
        driver.find_element_by_css_selector(".wand-dialog-text__btns>div").click()
    except WebDriverException as e:
        pass
    sleep_seconds = random.randint(10,20)
    print(f"will sleep {sleep_seconds}s ....")
    sleep(sleep_seconds)
    try:
        # 长时间刷新会出现无结果错误页面，点击无结果进行刷新
        no_result_ele = driver.find_element_by_class_name("g-noresult")
        no_result_ele.find_element_by_tag_name("h5").click()
        print("no result reload")
        return
    except WebDriverException as e:
        pass
    try:
        # 有折叠起来的排班信息的话 将折叠展开 不然获取不到里面的内容
        driver.find_element_by_class_name("cpt-book-workspace--expand").click()
    except WebDriverException as e:
        pass
    try:
        # 所有的排班信息所在的页面元素列表
        platform_elements = driver.find_elements_by_css_selector("ul[class='cpt-book-workspace--shift-item']>li")
    except WebDriverException as e:
        print(e)
        return
    if not platform_elements:
        print(f"none result {platform_elements}")
        return
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("*" * 25, now_time, "*" * 25)
    can_appointment = False
    for platform_element in platform_elements:
        content = platform_element.text
        print(">>>>>", content.replace('\n', ' ').strip())
        if content.endswith("预约"):
            can_appointment = True
    if can_appointment:
        print("*" * 28, "开始预约了", "*" * 28)
        playsound("261204262634929.mp3")
    else:
        print("*" * 28, "还不能预约", "*" * 28)
    driver.refresh()


if __name__ == '__main__':
    while True:
        fetch()
        sleep(10)
