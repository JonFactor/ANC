from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import re, os, json

# WebDriverWait(web, 100).until(EC.visibility_of_element_located(By.CLASS_NAME, 'asd'))

### settings
opt = Options()
opt.headless = True
web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

### getting websites
with open('python\websites.json', 'r') as f:
    string = f.read()
    d = json.loads(string)

### storage
import firebase_admin, json, requests
import google.cloud
from firebase_admin import credentials, firestore

## varibles
cred = credentials.Certificate("python/scraper-4e219-firebase-adminsdk-mz229-deff8437b5.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()
### colection
doc_ref = store.collection(u'starting')

### iterating
for link in d:

    try:
        ### pre condtions
        if link == '' or 'http' not in link:
            continue

        ### body
        web.get(link)

        pg = web.page_source
        reg = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

        emails = []
        for match in re.finditer(reg, pg):
            emails.append(match.group())

    except Exception:
        emails = 'error not found 404'

    ### commiting
    doc_ref.add({ u'names' : f'{link}' ,u'webstie' : f'{emails}' })

    print('done')



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