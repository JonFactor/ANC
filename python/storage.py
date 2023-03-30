import firebase_admin, json, requests
import google.cloud
from firebase_admin import credentials, firestore

## varibles
cred = credentials.Certificate("python/scraper-4e219-firebase-adminsdk-mz229-deff8437b5.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()
### colection
doc_ref = store.collection(u'starting')

### getting data
with open('python/stored-temp.json', 'r') as file:
    string = file.read()
    data = json.loads(string)
    name = data['name']
    mail = data['storage']

### commiting
doc_ref.add({ u'names' : f'{mail}' ,u'webstie' : f'{name}' })