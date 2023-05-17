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
import re, time


@ csrf_protect 
def scrap(request):

    # params
    totalEmailLimit = int(request.POST.get('page') )
    search = request.POST.get('search')

    # driver stuff
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

    #prequeists 
    regexEmail = r'''(?:[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
    totalEmails = []
    breaker = True

    # start
    driver.get('https://www.google.com/search?q='+search)

    containingLinks = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
    links = []
    for conatiners in containingLinks:
        links.append(conatiners.find_element(By.TAG_NAME, 'a').get_attribute('href'))
    for link in links:
        if not breaker: break
        driver.get(link) 
        repeats = 0
        pgSrc = driver.page_source
        for match in re.finditer(regexEmail, pgSrc):
            if len(totalEmails) >= totalEmailLimit: 
                breaker = False
                break
            totalEmails.append(match.group())
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
            url = (driver.current_url).split('/')[2]
            try:
                if url in href:
                    try: 
                        driver.get(href)
                        iteration += 1
                    except Exception: continue
            except Exception: pass
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
            else: pass

    driver.quit()

    return render(request, 'display.html', {'totalEmails': totalEmails})