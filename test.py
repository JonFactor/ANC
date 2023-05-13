# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

" WHY ASSIGNEMT NOW "
""""
Normally we would put assignet as close as we can to when we use
the varible for readablity, but selenium is demanding 
like by step dad and will beat us if we do even the 
simplist of operations while hes drinkn... i mean runing. 
"""

# driver stuff
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#prequeists 
url = 'https://maya.um.edu.my/sitsvision/wrd/siw_lgn'
regexEmail = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
totalEmails = []
printedEmails = []
totalSiteIter = 0
pastPageLoop = True
containerLoop = True

# params
unqiueSiteLimit = 3
perPgLimit = 5
siteLimit = 3
search="random emails"

def emailFinding(pgEmails, pgSrc):
    for match in re.finditer(regexEmail, pgSrc):
        if len(pgEmails) >= perPgLimit: 
            break
        else:
            pgEmails.append(match.group())

def totalSiteCheck():
    global totalSiteIter, siteLimit, pgEmails, totalEmails, initialPageLoop, pastPageLoop, containerLoop
    if totalSiteIter >= siteLimit: 
        if pgEmails != [] or '': 
            if pgEmails not in totalEmails:
                totalEmails.append(pgEmails)
            initialPageLoop = False
            pastPageLoop = False
            containerLoop = False
            return True
        return True
    else:
        return False

# start driver
driver.get('https://www.google.com/search?q='+search)

# meat
while containerLoop:
    initialPageLoop = True
    thisSiteIter = 0
    while initialPageLoop:
        try:
            websiteClicky = driver.find_elements(By.TAG_NAME, value='h3')[thisSiteIter].click()
            pgEmails = []
            pgSrc = driver.page_source
            emailFinding(pgEmails, pgSrc)
            thisSiteIter += 1
            totalSiteIter += 1
            containerLoop = False
            totalEmails.append(pgEmails)
            # if totalSiteCheck(): break
            break
        except Exception: pass
    thisSiteIter = 0
    while pastPageLoop:
        try:
            websiteLink = driver.find_elements(By.TAG_NAME, value='a')[thisSiteIter].get_attribute('href')
            driver.get(websiteLink)
            if driver.current_url == 'data:,': continue
            # if totalSiteCheck(): break
            pgEmails = []
            pgSrc = driver.page_source
            emailFinding(pgEmails, pgSrc)
            thisSiteIter += 1
            totalSiteIter += 1
            if pgEmails != [] or '': totalEmails.append(pgEmails)
            driver.back()
        except Exception:
            containerLoop = True
            pastPageLoop = False
            driver.back()
driver.quit()

print(totalEmails)