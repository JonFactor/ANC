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

# WebDriverWait(web, 100).until(EC.visibility_of_element_located(By.CLASS_NAME, 'asd'))
# https://mahoningctc.com/all-staff-directory/
# https://www.google.com/search?q=

opt = Options()
opt.headless = True
web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
d = ('mcctc staff')
web.get('https://www.google.com/search?q='+d)

ex = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

emails = []
printed = []

f = 0
totalhref = 0
y = 0
z = True
l = True
while l:
    j = True
    while j:
        try:
            click = web.find_elements(By.TAG_NAME, value='h3')[y]
            click.click()
            pg = web.page_source
            for match in re.finditer(ex, pg):
                emails.append(match.group())
            y += 1
            z = True
            l = False
            break
        except:
            y += 1
            pass
    while z:
        try:
            htag = web.find_elements(By.TAG_NAME, value='a')[f]
            g = htag.get_attribute('href')
            web.get(g)
            pg = web.page_source
            for match in re.finditer(ex, pg):
                emails.append(match.group())
            f += 1
            web.back()
        except Exception:
            for i, fix in enumerate(emails):
                if fix not in printed:
                    print(fix)
                    printed.append(fix)
            print('NO MORE HREFS')
            l = True
            f = 0
            web.back()
            z = False

# outside()
# inside()