from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import OrderedDict 
import re

opt = Options()
opt.headless = True
web = webdriver.Chrome(chrome_options=opt, service=Service(ChromeDriverManager().install()))
web.get('https://mahoningctc.com/')

links = web.find_elements(By.TAG_NAME, 'a')
for i in links:
    print(i.get_attribute('href'))
time.sleep(500)