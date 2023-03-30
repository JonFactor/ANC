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

# WebDriverWait(web, 100).until(EC.visibility_of_element_located(By.CLASS_NAME, 'asd'))
# https://mahoningctc.com/all-staff-directory/
# https://www.google.com/search?q=

opt = Options()
opt.headless = True
web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
d = 'mcctc'
web.get('https://www.google.com/search?q='+d)

goof = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

emails = []
printed = []

click = web.find_elements(By.TAG_NAME, value='h3')[0]
click.click()
time.sleep(1)
z = True
while z:
    f = 0
    htag = web.find_elements(By.TAG_NAME, value='a')[f]
    g = htag.get_attribute('href')
    web.get(g)
    pg = web.page_source
    for match in re.finditer(goof, pg):
        emails.append(match.group())
    for i, fix in enumerate(emails):
        if fix not in printed:
            print(fix)
            printed.append(fix)
    f+1
    time.sleep(2)
    web.back()
    time.sleep(1)


y = True
time.sleep(10)
# while True:
#     hrefs = web.find_elements(By.TAG_NAME, value='href')[i]
#     hrefs.click()
#     emails = []
#     printed = []
#     for match in re.finditer(goof, pg):
#         emails.append(match.group())
#     for i, fix in enumerate(emails):
#         if fix not in printed:
#             print(fix)
#             printed.append(fix)
#     i+1



# time.sleep(0.5)
# click = web.find_all(by=By.TAG_NAME, value='href')[0]



# emails = []
# printed = []
# for match in re.finditer(goof, pg):
#     emails.append(match.group())
# for i, fix in enumerate(emails):
#     if fix not in printed:
#         print(fix)
#         printed.append(fix)
    
# time.sleep(100)


























# while x:
#     try:
#         web.get(d)
#         x = False
#     except:
#         web.quit()
#         d = input('asd')
#         web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         web.get(d)

# loginButton = web.find_element(By.CLASS_NAME, "sppb-btn.sppb-btn-success.button-text")
# loginButton.click()
# username = web.find_elements(By.CLASS_NAME, "form-login")[0]
# password = web.find_elements(By.CLASS_NAME, "form-login")[1]
# signInButton = web.find_element(By.CLASS_NAME, "signIn-button")

# username.send_keys("cheeriosmilky4@gmail.com")
# password.send_keys("000C3CAa1cheerios")