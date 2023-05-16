
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re


totalEmailLimit = 100
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


def hrefCheck(href):
    url = (driver.current_url).split('/')[2]
    if href == None: return False
    if url in href:
        return True
    else:
        return False


def pageHandle():
    global breaker, totalEmails, driver

    repeats = 0
    pgSrc = driver.page_source
    for match in re.finditer(regexEmail, pgSrc):
        if len(totalEmails) >= totalEmailLimit: 
            breaker = False
            break
        if match.group() not in totalEmails:
            totalEmails.append(match.group())
        else: 
            repeats += 1
            print(repeats)

def handleInsideLinks():
    webstieLinks = driver.find_elements(By.TAG_NAME, 'a')
    websiteHrefs = []
    rabbitWholeLimit = 20
    for link in webstieLinks:
        linkHref = link.get_attribute('href')
        websiteHrefs.append(linkHref)
    iteration = 0
    for href in websiteHrefs:
        if iteration > rabbitWholeLimit: 
            break
        if hrefCheck(href):
            try: 
                driver.get(href)
                iteration += 1
            except Exception: continue
            pageHandle()
        else: pass

def getGoogleLinks():
    containingLinks = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
    links = []
    for conatiners in containingLinks:
        links.append(conatiners.find_element(By.TAG_NAME, 'a').get_attribute('href'))
    return links

# start
driver.get('https://www.google.com/search?q='+search)

links = getGoogleLinks()
for link in links:
    if not breaker: break
    driver.get(link) 
    pageHandle()
    handleInsideLinks()

driver.quit()

print(totalEmails)