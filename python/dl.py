import re
import urllib.parse
import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import math
import random
import time

os.environ["PATH"] += os.pathsep + os.path.abspath('../resources')

x = []
rootUrl = "C:/Users/ABM589/Downloads/test/"

with open("../resources/nbb.urls.txt") as urls:
    for url in urls:
        bce = url[-11:]
        folderUrl = rootUrl + bce[:-1]
        if not os.path.exists(folderUrl):
            os.makedirs(folderUrl)
        options = Options()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        prefs = {"profile.default_content_settings.popups": 0,"download.default_directory": folderUrl, "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(chrome_options=options)
        print (url)
        browser.get(url)
        elements = browser.find_elements_by_css_selector('.ui-commandlink.ui-widget.actioncommandlink')
        print (len(elements))
        actions = ActionChains(browser)
        i = 0
        for element in elements:
            if i < 12:
                ActionChains(browser).move_to_element(element).click(element).perform()
                time.sleep(float(random.randint(300, 500) / 1000))
            i += 1
        browser.close()

