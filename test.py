# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import OrderedDict 
import re, json


 # driver stuff
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#prequeists 
url = 'https://maya.um.edu.my/sitsvision/wrd/siw_lgn'
ex = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
emails = []
printed = []
f = 0
y = 0
z = True
l = True

search="mcctc staff directory"
# start driver
driver.get('https://www.google.com/search?q='+search)

# meat

while l:
    j = True
    success = 0
    while j:
        try:
            click = driver.find_elements(By.TAG_NAME, value='h3')[y]
            click.click()
            pg = driver.page_source
            for match in re.finditer(ex, pg):
                emails.append(match.group())
            y += 1
            z = True
            l = False
            success += 1
            break
        except:
            y += 1
            pass
        if success >= 5: break
    while z:
        try:
            htag = driver.find_elements(By.TAG_NAME, value='a')[f]
            g = htag.get_attribute('href')
            driver.get(g)
            pg = driver.page_source
            for match in re.finditer(ex, pg):
                emails.append(match.group())
            f += 1
            driver.back()
        except Exception:
            for i, fix in enumerate(emails):
                if fix not in printed:
                    print(fix)
                    printed.append(fix)
            print('NO MORE HREFS')
            l = True
            f = 0
            driver.back()
            z = False

# end driver
driver.quit()