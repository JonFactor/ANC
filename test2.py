
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re


totalEmailLimit = 30
search = 'random emails'

# driver stuff
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#prequeists 
regexEmail = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
totalEmails = []
breaker = True

def emailFinding(pgEmails, pgSrc):
    for match in re.finditer(regexEmail, pgSrc):
        pgEmails.append(match.group())

def pageHandle():
    global breaker, totalEmails, driver

    pgSrc = driver.page_source
    for match in re.finditer(regexEmail, pgSrc):
        if len(totalEmails) >= totalEmailLimit: 
            breaker = False
            break
        else:
            totalEmails.append(match.group())

def handleInsideLinks():
    webstieLinks = driver.find_elements(By.TAG_NAME, 'a')
    websiteHrefs = []
    for link in webstieLinks:
        websiteHrefs.append(link.get_attribute('href'))
    for href in websiteHrefs:
        driver.get(href)
        pageHandle()

driver.get('https://www.google.com/search?q='+search)

links = driver.find_elements(By.TAG_NAME, 'h3')
for link in links:
    link.click()            # goto site
    pageHandle()
    handleInsideLinks()
    driver.get('https://www.google.com/search?q='+search)


driver.quit()