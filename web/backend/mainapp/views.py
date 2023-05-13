from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import  csrf_protect 
# Create your views here.

@csrf_protect 
def mainapp(request):
    return render(request, 'mainapp.html', {})

def display(request, totalEmails = ''):
    return render(request, 'display.html', {totalEmails})

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

#models
from .models import Result

@ csrf_protect 
def scrap(request):

    siteLimit = request.POST.get('page')
    search = request.POST.get('search')
    perPgLimit = request.POST.get('email')

    # driver stuff
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    #prequeists 
    regexEmail = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
    totalEmails = []
    totalSiteIter = 0
    pastPageLoop = True
    containerLoop = True

    def emailFinding(pgEmails, pgSrc):
        for match in re.finditer(regexEmail, pgSrc):
            if len(pgEmails) >= int(perPgLimit): break
            else: pgEmails.append(match.group())

    driver.get('https://www.google.com/search?q='+search)
    while containerLoop:
        initialPageLoop = True
        thisSiteIter = 0
        while initialPageLoop:
            try:
                driver.find_elements(By.TAG_NAME, value='h3')[thisSiteIter].click()
                pgEmails = []
                pgSrc = driver.page_source
                emailFinding(pgEmails, pgSrc)
                thisSiteIter += 1
                totalSiteIter += 1
                containerLoop = False
                totalEmails.append(pgEmails)
                if totalSiteIter >= siteLimit: 
                    if pgEmails != [] or '' or pgEmails not in totalEmails: 
                        totalEmails.append(pgEmails)
                    initialPageLoop = False
                    pastPageLoop = False
                    containerLoop = False
                    break
                break
            except Exception: pass
        thisSiteIter = 0
        while pastPageLoop:
            try:
                driver.get(driver.find_elements(By.TAG_NAME, value='a')[thisSiteIter].get_attribute('href'))
                if driver.current_url == 'data:,': continue
                if totalSiteIter >= siteLimit: 
                    if pgEmails != [] or '' or pgEmails not in totalEmails: 
                        totalEmails.append(pgEmails)
                    initialPageLoop = False
                    pastPageLoop = False
                    containerLoop = False
                    break
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

    return render(request, 'display.html', {'totalEmails': totalEmails})