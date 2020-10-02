import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('your firebase service account key')
firebase_admin.initialize_app(cred)

db = firestore.client()

#writing data to firestore
doc_ref = db.collection('Your Collection').document('Your Document')
doc_ref.set({
    'id of your choice':'Data value'
})

#reading data from firestore
emp_ref = db.collection('Your Collection')
docs = emp_ref.stream()

for doc in docs:
    print('{} => {}'.format(doc.id, doc.to_dict()))
    #You will get what the above statement when you run the program successfully