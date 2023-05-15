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


@ csrf_protect 
def scrap(request):

    totalEmailLimit = int(request.POST.get('page') )
    search = request.POST.get('search')

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
            pgEmails.append(match.group())

    driver.get('https://www.google.com/search?q='+search)
    clickSiteIter = 0
    while containerLoop:
        initialPageLoop = True
        while initialPageLoop:
            try:
                driver.find_elements(By.TAG_NAME, value='h3')[clickSiteIter].click()
                clickSiteIter += 1
                pgEmails = []
                pgSrc = driver.page_source
                emailFinding(pgEmails, pgSrc)
                if pgEmails != [] or '' or pgEmails not in totalEmails: 
                    totalSiteIter += len(pgEmails)
                    pgEmails = pgEmails[:totalEmailLimit]
                    totalEmails.append(pgEmails)
                break
            except Exception: break
        hrefSiteIter = 0
        pastPageLoop = True
        while pastPageLoop:
            try:
                link = driver.find_elements(By.TAG_NAME, value='a')[hrefSiteIter].get_attribute('href')
                driver.get(link)
                if driver.current_url == 'data:,': continue
                hrefSiteIter += 1
                pgEmails = []
                pgSrc = driver.page_source
                emailFinding(pgEmails, pgSrc)
                print('23333')
                if pgEmails != [] or '' or pgEmails not in totalEmails: 
                    totalSiteIter += len(pgEmails)
                    pgEmails = pgEmails[:totalEmailLimit]
                    totalEmails.append(pgEmails)
                if totalSiteIter > totalEmailLimit: 
                    print('gay')
                    containerLoop = False
                    pastPageLoop = False 
                    initialPageLoop = False
                    break
                driver.back()
            except Exception:
                containerLoop = True
                pastPageLoop = False
                driver.back()
    driver.quit()

    return render(request, 'display.html', {'totalEmails': totalEmails})